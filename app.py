from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello World", "Application": "Team Application"})



if __name__ == '__main__':
    app.run(debug=True, port=8001, host='0.0.0.0') 