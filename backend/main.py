
    
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from groq import Client
from dotenv import load_dotenv
from pathlib import Path
import re
import subprocess
import cloudinary
import cloudinary.uploader
from typing import Optional
from gtts import gTTS


from manim import config

config["media_dir"] = "/app/media"
config["preview"] = False
config["show_in_file_browser"] = False

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
client = Client(api_key=groq_api_key)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cloudname = os.getenv("CLOUD_NAME")
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

cloudinary.config(
    cloud_name=cloudname,
    api_key=api_key,
    api_secret=api_secret
)

class Post(BaseModel):
    requirements: str
    voice: Optional[str] = None

@app.get('/')
def root():
    return {"message": "Manim Video Generation API"}

@app.post("/usercase")
def user_requirements(usercase: Post):
    try:
          
        prompt = [
         {
        "role": "system",
        "content": (
            "You are an expert Python developer specializing in Manim. "
            "Generate clean, working Manim scripts using only the `Text` class (not `Tex`), "
            # "and avoid any dependencies on LaTeX, MiKTeX, or MathJax. "
            "Do not use or include any math rendering that relies on LaTeX. "
            "Only use built-in Manim features like `Text`, `Square`, `Circle`, `Line`, etc. "
            "Include visual animations with smooth transitions and balanced spacing. "
            "Avoid cluttered scenes and do not use arrows unless essential. "
            "Always use `animate` with Mobjects in `self.play(...)` (e.g., `self.play(mob.animate.move_to(UP))`) — "
            "never pass raw method calls like `mob.move_to(UP)` directly to `play`. "
            "Return ONLY the Manim Python code with no explanations or extra text."
        )
        },
        {
        "role": "user",
        "content": usercase.requirements  # or replace with a string like "Show 'Welcome to AI' text and fade it out."
        }
        ]
        
        response = client.chat.completions.create(
            model="mistral-saba-24b",
            messages=prompt,
            temperature=0.3
        )

        
        full_response = response.choices[0].message.content
        match = re.search(r"```(?:python)?\n(.*?)```", full_response, re.DOTALL)
        manim_code = match.group(1).strip() if match else full_response.strip()

        
        file_path = Path("generated_scene.py")
        file_path.write_text(manim_code)

        
        class_match = re.search(r"class\s+(\w+)\(Scene\):", manim_code)
        if not class_match:
            return {"error": "No valid Scene class found"}
        class_name = class_match.group(1)

        
        render_command = [
            "manim",
            "--media_dir", "/app/media",
            "-ql",
            str(file_path),
            class_name
        ]

        subprocess.run(render_command, check=True)

        
        input_video_path = Path(f"/app/media/videos/generated_scene/480p15/{class_name}.mp4")
        
        
        final_video_path = input_video_path
        if usercase.voice:
            audio_path = Path("/app/media/voice.mp3")
            tts = gTTS(text=usercase.voice)
            tts.save(audio_path)

            final_video_path = Path(f"/app/media/final_{class_name}.mp4")
            
            ffmpeg_command = [
                "ffmpeg", "-y",
                "-i", str(input_video_path),
                "-i", str(audio_path),
                "-c:v", "copy",
                "-c:a", "aac",
                "-shortest",
                str(final_video_path)
            ]
            subprocess.run(ffmpeg_command, check=True)

        
        upload_result = cloudinary.uploader.upload_large(
            str(final_video_path),
            resource_type="video"
        )

        return {
            "code": manim_code,
            "url": upload_result["secure_url"]
        }

    except subprocess.CalledProcessError as e:
        return {"error": "Video processing failed", "details": str(e)}
    except Exception as e:
        return {"error": "Unexpected error", "details": str(e)}



   
  



    




