import os, time
from fastapi import FastAPI
from pydantic import BaseModel
from pageindex import PageIndexClient
from dotenv import load_dotenv
load_dotenv()

# --- Config ---
API_KEY = os.getenv("PAGEINDEX_API_KEY")
PDF_PATH = "./document.pdf"

# --- Setup ---
client = PageIndexClient(api_key=API_KEY)
app = FastAPI()
doc_id = None

# --- PDF Upload on startup ---
@app.on_event("startup")
def startup():
    global doc_id
    print("PDF is uploading...")
    result = client.submit_document(PDF_PATH)
    doc_id = result["doc_id"]
    print(f"doc_id: {doc_id} | Processing...")

    while True:
        status = client.get_document(doc_id)["status"]
        if status == "completed":
            print("Ready!")
            break
        time.sleep(5)

# --- Search Route ---
class Query(BaseModel):
    q: str

@app.post("/search")
def search(body: Query):
    response = client.chat_completions(
        messages=[{"role": "user", "content": body.q}],
        doc_id=doc_id
    )
    return {"answer": response["choices"][0]["message"]["content"]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8011, reload=True)
