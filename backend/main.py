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
load_dotenv()
groq_pai_key=os.getenv("GROQ_API_KEY")
client=Client(api_key=groq_pai_key)




app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cloudname=os.getenv("CLOUD_NAME")
api_key=os.getenv("API_KEY")
api_secret=os.getenv("API_SECRET")


cloudinary.config(
    cloud_name=cloudname,
    api_key=api_key,
    api_secret=api_secret
)




class Post(BaseModel):
    requirements:str



@app.get('/')
def root():
    return {"message":"Hello world"}



@app.post("/usercase")
def userrequirements(usercase:Post):
    print(f"user sent this particualr details {usercase}")
    prompt = [
    {"role": "system", "content":"You are a Python developer that writes Manim code based on user descriptions. Only return the Manim python script  code only nothing else .Do not send the text also.Give me Manim code that does not require LaTeX or MiKTeX. Use Text() instead of Tex(), and avoid anything that depends on LaTeX compilation. Include shapes, arrows, and animations that work in a clean scene and keep proper gaps"},
    {"role": "user", "content": usercase.requirements}

    
    ]
    response=client.chat.completions.create(
       
        model="mistral-saba-24b",
        messages=prompt,
        temperature=0.3

    )

    full_response = response.choices[0].message.content

    match = re.search(r"```(?:python)?\n(.*?)```", full_response, re.DOTALL)

    if match:
        manim_code = match.group(1).strip()
       

    else:
        
        print(f"i am inside the else block")
        manim_code = full_response.strip()
    print(f"i got the code here it is {manim_code}")
    file_path=Path("generated_scene.py")
    file_path.write_text(manim_code)
    class_match=re.search(r"class\s+(\w+)\(Scene\):",manim_code)
    if not class_match:
        return {"error":"No scene calss found in the generator code"}
    class_name=class_match.group(1)
    try:
        subprocess.run([
            "manim",  
            str(file_path),
            class_name,
            "-pql", 
        ], check=True)
    except subprocess.CalledProcessError as e:
        return {"error": "Failed to render with Manim", "details": str(e)}
    
    upload_rsult=cloudinary.uploader.upload_large(
        f"media/videos/generated_scene/480p15/{class_name}.mp4",
        resource_type="video"
    )
    video_url=upload_rsult["secure_url"]
    return {"code":manim_code,"url":video_url}
    


    


   
    




  
     






   
  



    



