from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "SSRF redirect is ready."

@app.route("/redirect")
def ssrf_redirect():
    url = request.args.get("url")
    try:
        r = requests.get(url, timeout=3)
        return f"<pre>{r.text}</pre>"
    except Exception as e:
        return f"Failed to fetch URL: {e}"

if __name__ == "__main__":
    app.run()
