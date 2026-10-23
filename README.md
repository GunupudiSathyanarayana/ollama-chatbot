# Ollama Chatbot

A small chatbot web application built with Streamlit, LangChain, and Ollama. It sends the prompt entered in the browser to the locally hosted `llama2` model and displays the model's response.

## Requirements

- Python 3.9 or later
- [Ollama](https://ollama.com/) installed and running locally
- The `llama2` model downloaded in Ollama

The application uses Ollama's default local server address: `http://localhost:11434`.

## Run locally

1. **Download the model and make sure Ollama is running.** In a terminal, run:

   ```powershell
   ollama pull llama2
   ```

   Ollama normally starts its local server automatically. If it is not running, start Ollama before launching the app. You can verify the server is reachable at `http://localhost:11434`.

2. **Create and activate a Python virtual environment** from the project directory:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux, activate it with:

   ```bash
   source .venv/bin/activate
   ```

3. **Install the dependencies:**

   ```bash
   python -m pip install -r requirements.txt
   ```

4. **Configure LangSmith.** The application enables LangSmith tracing and reads these values from the project-root `.env` file:

   ```dotenv
   LANGSMITH_API_KEY=your_langsmith_api_key
   LANGSMITH_ENDPOINT=https://api.smith.langchain.com
   LANGSMITH_PROJECT=your_project_name
   ```

   Set `LANGSMITH_API_KEY` to your own key. Keep the `.env` file private and do not commit real credentials.

5. **Start the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

   Open the local URL printed by Streamlit (normally `http://localhost:8501`) and enter a prompt.

## Project files

- `app.py` — Streamlit interface and LangChain pipeline that calls Ollama's `llama2` model.
- `requirements.txt` — Python package dependencies.
- `.env` — Local LangSmith configuration; keep credentials private.
