from flask import Flask, request
from emails.funcs.adaptador import adapter

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/email_sender", methods=['POST'])
def send_message():
    adapter(request.json)
    return {"status": 200,
            "message": "Mails enviados"}


if __name__ == '__main__':
    app.run(debug=True)