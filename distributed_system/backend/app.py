from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Serve index.html from /app/frontend, which is the actual path inside the container
@app.route("/")
def serve_index():
    return send_from_directory("frontend", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
