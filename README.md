# DSA Learning Assistant

An interactive Data Structures and Algorithms (DSA) Learning Assistant with a Python sandbox. Learn DSA with an AI mentor, execute code in the browser, and trace algorithms using interactive visualizers.

## Try it out!

🚀 **[Access here](https://dsa-learning-assistant.onrender.com/)**

## Features

- **Interactive AI Tutor**: Chat with an AI mentor to learn about arrays, stacks, trees, sorting algorithms, and more.
- **Python Sandbox**: Write and execute Python scripts directly in your browser using Pyodide.
- **Visualizers**: Interactive visualizers for Data Structures (Arrays, Stacks, Queues, Linked Lists, Trees, Hash Tables, etc.).
- **Premium UI**: Modern OLED dark mode and crisp light mode aesthetics featuring Vercel's Geist font, glassmorphism, and floating hover effects.
- **Responsive Design**: Carefully crafted to look great and function smoothly.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (CodeMirror for code editing, Highlight.js for syntax highlighting)
- **Backend**: Python, Flask, Gunicorn
- **Containerization**: Docker

## Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/lidostark/dsa-learning-assistant.git
   cd dsa-learning-assistant
   ```

2. Make sure you have a `.env` file with your necessary environment variables (like API keys).

3. Build the Docker container:
   ```bash
   docker build -t dsa-assistant .
   ```

4. Run the container:
   ```bash
   docker run -p 10000:10000 --env-file .env dsa-assistant
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:10000
   ```
