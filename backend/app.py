from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your DeepSeek API URL and key
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat"
DEEPSEEK_API_KEY = "your_deepseek_api_key"

@app.route("/chat", methods=["POST"])
def chat():
    # Get user input from the frontend
    user_input = request.json.get("text")

    # Send the input to DeepSeek API
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    data = {"prompt": user_input, "language": "am"}
    response = requests.post(DEEPSEEK_API_URL, json=data, headers=headers)

    # Return the response to the frontend
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
