import os
from pathlib import Path
from google import genai
from google.genai import types

env_path = Path(__file__).resolve().parent / ".env"
if env_path.exists():
    try:
        from dotenv import load_dotenv
    except ImportError as exc:
        raise ImportError("python-dotenv is required to load .env. Install it with `pip install python-dotenv`.") from exc
    load_dotenv(env_path)

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file or your shell environment.")

client = genai.Client(api_key=api_key)

#adding system instructions to the request
SYSTEM_INSTRUCTION = """You are a Data Structures and Algorithms (DSA) tutor for an intermediate Python programmer who is just starting to learn DSA concepts.

Your rules:
1. Explain concepts step-by-step, starting from the intuition before diving into implementation.
2. Always use Python for code examples.
3. When explaining a data structure, cover: what it is, why it exists, when to use it, and a simple Python implementation.
4. When explaining an algorithm, cover: the problem it solves, the intuition behind it, step-by-step walkthrough with a small example, Python code, and time/space complexity.
5. Keep explanations concise but thorough. Use analogies when helpful.
6. If the user asks a vague question, ask a clarifying question before answering.
7. Encourage the user and suggest related topics they might want to explore next."""

#chat session with the model
chat = client.chats.create(
    model='gemini-3.1-flash-lite',
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION
    ),
)

print('DSA Learning Assistant (terminal mode)')
print("Type 'quit' to exit.\n")

while True:
    user_input = input('You: ')
    if user_input.lower() == 'quit':
        break
    response = chat.send_message(message=user_input)
    print(f'\nAssistant: {response.text}\n')