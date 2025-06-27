from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from app.generator import generate_video

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate(prompt_request: PromptRequest):
    try:
        video_path = generate_video(prompt_request.prompt)
        return {"video_path": video_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Text-to-Video Generation API is running."}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
