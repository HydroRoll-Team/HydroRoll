from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['POST']) # type: ignore
def handle():
    payload = request.content_type
    print(payload)
    # return json.loads(payload)

if __name__ == '__main__':
    app.run('127.0.0.1',3000)