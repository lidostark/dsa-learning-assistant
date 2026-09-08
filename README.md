# DSA Learning Assistant

An interactive Data Structures and Algorithms (DSA) Learning Assistant with a Python sandbox. Learn DSA with an AI mentor, execute code in the browser, and trace algorithms using interactive visualizers.

## Try it out!

🚀 **[Access here](https://dsa-learning-assistant.onrender.com/)**

## Features

- **Interactive AI Tutor**: Chat with an AI mentor to learn about arrays, stacks, trees, sorting algorithms, and more.
- **Python Sandbox**: Write and execute Python scripts directly in your browser using Pyodide.
- **Visualizers**: Interactive visualizers for Data Structures (Arrays, Stacks, Queues, Linked Lists, Trees, Hash Tables, etc.).
- **Geist Design System**: Built on Vercel's Geist design language — near-black ink on a near-white canvas, hairline-bordered surfaces, and Geist Sans / Geist Mono throughout. Ships with a light default and an inverted dark theme.
- **Responsive Design**: Carefully crafted to look great and function smoothly.

## Design

The interface implements [Vercel's Geist design language](https://vercel.com/geist). The whole system is driven by CSS custom properties declared on `:root`, so retheming happens in one place.

- **Colour**: a single near-black ink (`#171717`) carries headings, body copy, primary buttons and borders on a near-white canvas (`#fafafa`), stepped through an ink → body → mute → faint text ladder. The accent blue (`#0070f3`) is reserved for links, focus and active states.
- **Type**: Geist Sans for UI and prose, Geist Mono for code and the uppercase section eyebrows. Weight is binary — 600 for headings, 500 for buttons and labels, 400 for everything else — and display type carries tight negative tracking.
- **Shape & depth**: 6px radius on functional chrome (buttons, inputs), 12–16px on content cards. Surfaces are defined by a 1px hairline first; shadows are whisper-soft and used sparingly.
- **The one flourish**: a soft multi-stop mesh gradient (cyan → blue → violet → magenta → amber) blooms behind the welcome headline. Nothing else on the page carries a decorative gradient.
- **Themes**: light is the default. `[data-theme="dark"]` swaps in the inverted Geist palette, and the toggle persists the choice to `localStorage`.

Code is rendered through one shared syntax palette, so a snippet reads identically in the sandbox editor (CodeMirror) and in the chat transcript (Highlight.js), in both themes.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript (CodeMirror for code editing, Highlight.js for syntax highlighting, Pyodide for in-browser Python)
- **Fonts**: Geist Sans & Geist Mono
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
