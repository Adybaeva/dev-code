# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Python Flask!  This is a new copy of our container!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
