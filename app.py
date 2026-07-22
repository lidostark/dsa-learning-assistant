import os
import uuid
from pathlib import Path

# pyrefly: ignore [missing-import]
from flask import Flask, render_template, request, jsonify, session
from google import genai
from google.genai import types

# Create the flask app
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dsa-learning-assistant-secret-key-1289")

env_path = Path(__file__).resolve().parent / ".env"
if env_path.exists():
    try:
        from dotenv import load_dotenv
    except ImportError as exc:
        raise ImportError("python-dotenv is required to load .env. Install it with `pip install python-dotenv`.") from exc
    load_dotenv(env_path)

# Reuse the same Gemini client from assistant.py
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file or your shell environment.")

client = genai.Client(api_key=api_key)

# Same system instructions as in assistant.py that shapes the tutor persona 
SYSTEM_INSTRUCTION = """You are a Data Structures and Algorithms (DSA) tutor for an intermediate Python programmer who is just starting to learn DSA concepts.

Your rules:
1. Explain concepts step-by-step, starting from the intuition before diving into implementation.
2. Always use Python for code examples.
3. When explaining a data structure, cover: what it is, why it exists, when to use it, and a simple Python implementation.
4. When explaining an algorithm, cover: the problem it solves, the intuition behind it, step-by-step walkthrough with a small example, Python code, and time/space complexity.
5. Keep explanations concise but thorough. Use analogies when helpful.
6. If the user asks a vague question, ask a clarifying question before answering.
7. Encourage the user and suggest related topics they might want to explore next."""

# Dictionary to hold the active chat sessions keyed by session_id
chat_sessions = {}

def get_chat_session():
    # Get or create a session ID for this visitor
    session_id = session.get('session_id')
    if not session_id or session_id not in chat_sessions:
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
        chat_sessions[session_id] = client.chats.create(
            model='gemini-3.1-flash-lite',
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION
            )
        )
    return chat_sessions[session_id]

@app.route('/')
def index():
    # Make sure session is initialized
    get_chat_session()
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Read the user's message from the JSON body
    user_message = request.json.get('message', '')
    session_chat = get_chat_session()
    try:
        response = session_chat.send_message(message=user_message)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reset', methods=['POST'])
def reset():
    # Remove the user's chat session from our active cache
    session_id = session.get('session_id')
    if session_id in chat_sessions:
        del chat_sessions[session_id]

    # Generate a fresh session ID and initialize a new chat session
    new_session_id = str(uuid.uuid4())
    session['session_id'] = new_session_id
    chat_sessions[new_session_id] = client.chats.create(
        model='gemini-3.1-flash-lite',
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION
        )
    )
    return jsonify({'status': 'success', 'message': 'Chat session reset successfully.'})

@app.route('/health')
def health():
    # check health of the app and return the status
    from datetime import datetime, timezone
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}, 200

if __name__ == '__main__':
    app.run(debug=True)