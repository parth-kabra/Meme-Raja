from flask import Flask
from threading import Thread

app = Flask("fatbatman")

@app.route("/")
def home():
    return "hi, i am alive"

def run():
    app.run(host = "0.0.0.0", port = 8080)

def keep_alive():
    t = Thread(target = run)
    t.start()