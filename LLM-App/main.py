from common import get_client

# with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:
#     response = client.chat.send(
#         model="openai/gpt-4o-mini",
#         messages=[
#             {"role": "user", "content": "Give me a single sentence motivational quote."}
#         ],
#         max_tokens=500
#     )

#     print(response.choices[0].message.content)

client = get_client()

while True:
    user_input = input("You: ")
    if user_input.lower()=="exit":
        break
    with client.messages.stream(
        model="claude-haiku-4-5-20251001",
        system="You are a helpful AI assistant",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        max_tokens=500,
        temperature=0.8
    ) as stream:
        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)