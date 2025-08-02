from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the workshop app!"

@app.route("/message")
def message():
    # serve the static file from ../data
    return send_file("../data/message.txt")

if __name__ == "__main__":
    # listen on all interfaces so curl localhost works, port 8000
    app.run(host="0.0.0.0", port=8000)
