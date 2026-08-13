from flask import Flask, request
from calculator import divide

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/divide", methods=["POST"])
def divide_route():
    data = request.get_json()
    a = data["a"]
    b = data["b"]
    try:
        result = divide(a, b)
        return {"result": result}
    except ValueError as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)
