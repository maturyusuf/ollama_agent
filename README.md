# 🦙 PDF Question Answering with LangChain, Ollama & Chroma

This project lets you ask questions about a PDF file using a local LLM (Llama 3 via Ollama). It retrieves relevant context from the PDF and generates accurate, concise answers.

### 🚀 Features
- Uses **LangChain** and **Ollama** (Llama 3) for local LLM-based answering.
- Embeds PDF text with `mxbai-embed-large` using **OllamaEmbeddings**.
- Stores and searches context with **Chroma vector store**.
- Simple terminal interface for chatting with your PDF.

### 📂 Files
- `main.py`: The main loop for asking questions.
- `vector.py`: Loads PDF, creates embeddings, and sets up the retriever.
- `data/summary.pdf`: Your source document.

### ▶️ How to Use
1. Place your `summary.pdf` inside the `data/` folder.
2. Run the script:
   ```bash
   python main.py
   ```
3. Ask any question about the PDF content!

### 🛠️ Requirements
- Python 3.9+
- [Ollama](https://ollama.com/) installed and running
- Models used:
  - `llama3.2` (for answering)
  - `mxbai-embed-large` (for embeddings)

---

**Example**  
```text
Enter your question (or 'exit' to quit): What is the main idea of the document?
```

---
```
