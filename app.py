from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route("/get_authentication_accounts")
def get_authentication_accounts():
    url = "http://127.0.0.1:8000/authentication"
    response = requests.get(url)
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(debug=True, port=8001, host='0.0.0.0') 