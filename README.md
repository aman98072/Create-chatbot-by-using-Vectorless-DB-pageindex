Here's the corrected file:

````markdown
# PageIndex RAG

Search your PDF from the terminal using FastAPI + PageIndex — no vectors, no embeddings, pure LLM reasoning.

## Setup

**1. Clone the repo:**

```bash
git clone https://github.com/aman98072/Create-chatbot-by-using-Vectorless-DB-pageindex
cd pageindex-rag
pip install fastapi uvicorn pageindex python-dotenv requests
```

**2. Create a `.env` file:**

```
PAGEINDEX_API_KEY=your_key_here   # dash.pageindex.ai se lo
```

Get your API key from [dash.pageindex.ai](https://dash.pageindex.ai)

**3. Set your PDF path in `main.py`:**

```python
PDF_PATH = "./document.pdf"
```

**4. Start the server:**

```bash
uvicorn main:app --reload
```

The server will start, upload your PDF, and wait for your queries.

## Usage

**Single query:**
```bash
python ask.py <user_query>
```
````