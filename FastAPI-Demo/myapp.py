from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class PromptRequest(BaseModel):
    message: str


class PromptResponse(BaseModel):
    message: str
    model: str
    status: str


@app.post("/generate")
def generate(request: PromptRequest):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": request.message}],
        temperature=0.8
    )
    return PromptResponse(
        message=response.choices[0].message.content,
        model="llama-3.3-70b-versatile",
        status="success"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("myapp:app", host="localhost", port=8000, reload=True)
