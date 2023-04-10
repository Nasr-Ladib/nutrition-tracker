from flask import Flask, jsonify, request
from src.nutrition import calculate_nutrition

app = Flask(__name__)

@app.route("/nutrition", methods=["POST"])
def nutrition():
    items = request.json.get("items")
    result = calculate_nutrition(items)
    return jsonify(result)

if __name__ == "__main__":
    app.run()