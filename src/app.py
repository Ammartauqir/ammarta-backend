from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/info")
def get_info():
    return jsonify({"message": "Hello, World! from Flask backend"})

if __name__ == "__main__":
    app.run(debug=True)

