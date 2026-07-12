import gradio as gr
from groq import Groq
from dotenv import load_dotenv
import os
import spaces

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@spaces.GPU
def chat_response(message, history):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": message}],
        temperature=0.8
    )
    return response.choices[0].message.content

with gr.Blocks(theme="soft") as demo:
    gr.ChatInterface(
        title="Simple Chat Assistant",
        description="A basic gradio chat interface example",
        examples=["Tell me a joke", "Give me a motivational quote of the day", "How are you?"],
        fn=chat_response
    )

if __name__ == "__main__":
    demo.launch(share=True)