
"use client"
import { useState } from "react"
import axios from "axios"


const calSansStyles = `
@import url('https://fonts.googleapis.com/css2?family=Cal+Sans&display=swap');

.cal-sans {
  font-family: "Cal Sans", sans-serif;
  font-weight: 400;
  font-style: normal;
}`

export default function VideoRequirementForm() {
  const [input, setInput] = useState('')
  const [videoUrl, setVideoUrl] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [voiceinput,setvoiceinput]=useState<string|null>(null)
  
  async function changeHandler(e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) {
    setInput(e.target.value)
  }

  async function voicechangrhandler(e:React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>)
  {
        setvoiceinput(e.target.value) 
  }
  
  async function submitHandler(e:any) {
    e.preventDefault()
    setIsLoading(true)
    
    try {


         if (input)
         {
          const response:any = await axios.post('https://ai-harkirat.onrender.com/usercase', {
            requirements: input,
            voice:voiceinput
          })

          console.log(response.data.url)
          let videoUrl = response.data.url


          if (videoUrl) {
            setVideoUrl(videoUrl)
            setInput("")
          }


          setvoiceinput("")
         }
       
    
    
    } catch (error) {
      console.error("Error fetching video:", error)
    } finally {
      setIsLoading(false)
    }
  }
  
  return (
    <div className="min-h-screen w-full bg-gradient-to-b from-blue-50 to-white flex flex-col">
      <style>{calSansStyles}</style>
      
     
      <header className="w-full bg-white shadow-md py-8">
        <div className="w-full px-6">
          <h1 className="text-5xl cal-sans font-bold text-center text-black">AI Animator Studio</h1>
          <p className="text-xl cal-sans text-center text-gray-600 mt-3">Create stunning animated videos with just a text prompt</p>
        </div>
      </header>
      
     
      <main className="flex-grow w-full px-6 py-8">
        <div className="flex flex-col lg:flex-row gap-8">
         
          <div className="w-full lg:w-1/2 bg-white rounded-xl shadow-lg p-8 border border-gray-200">
            <h2 className="text-3xl cal-sans font-bold text-black mb-4">Video Generator</h2>
            <p className="text-gray-600 mb-6 cal-sans text-lg">
              Describe the animation you want to create. Be specific about style, content, and mood for best results.
            </p>
            
            <textarea
              placeholder="Enter your animation requirements in detail..."
              value={input}
              onChange={changeHandler}
              className="w-full px-6 py-5 rounded-lg border-2 border-gray-300 text-black focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-lg cal-sans h-40"
            />

            
            <input
  type="text"
  placeholder="Enter the text message u want in this video"
  onChange={voicechangrhandler}
  value={voiceinput || ""}
  className="w-full mt-4 px-4 py-3 rounded-lg border-2 border-gray-300 text-black focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-lg cal-sans"
/>


            
            <button 
              onClick={submitHandler}
              disabled={!input || isLoading}
              className="w-full mt-6 text-white font-bold py-4 px-6 rounded-lg transition duration-300 text-xl cal-sans disabled:opacity-50 disabled:cursor-not-allowed bg-blue-600 hover:bg-blue-700"
            >
              {isLoading ? (
                <span className="flex items-center justify-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Processing...
                </span>
              ) : (
                "Generate Video"
              )}
            </button>
          </div>
          
         
          <div className={`w-full lg:w-1/2 bg-white rounded-xl shadow-lg p-8 border border-gray-200 ${!videoUrl && 'flex items-center justify-center'}`}>
            {videoUrl ? (
              <>
                <h2 className="text-3xl cal-sans font-bold text-black mb-4">Your Generated Video</h2>
                <p className="text-gray-600 mb-6 cal-sans text-lg">
                  Here's your AI-generated animation based on your requirements.
                </p>
                <video
                  src={videoUrl}
                  controls
                  className="w-full rounded-md shadow-md"
                />
              </>
            ) : (
              <div className="text-center py-16">
                <p className="text-2xl cal-sans text-gray-400">Video will appear here</p>
                <p className="text-gray-400 cal-sans mt-2">Generate a video using the form on the left</p>
              </div>
            )}
          </div>
        </div>
      </main>
      
     
      <footer className="w-full bg-gray-100 py-6">
        <div className="w-full text-center text-gray-600">
          <p className="cal-sans">Adding More Features Soon🎯</p>
        </div>
      </footer>
    </div>
  )
}