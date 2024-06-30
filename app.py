#Run this at the start of every terminal session
#source .venv/bin/activate
#URL: http://127.0.0.1:5000/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '_main_':
    app.run()