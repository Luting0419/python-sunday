from flask import Flask

app = Flask(__name__)
@app.route("/health")
@app.route("/")
def hello():
    return "<H1>Hello, 世界!</H1>"