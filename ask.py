import sys, requests

query = " ".join(sys.argv[1:])
if not query:
    print("Usage: python ask.py <your question>")
    sys.exit()

r = requests.post("http://localhost:8011/search", json={"q": query})
print("\n" + r.json()["answer"])