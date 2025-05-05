from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Simple chatbot logic ---
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."

# --- API endpoint ---
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = get_response(user_input)
    return jsonify({"response": response})

# --- Run the app ---
if __name__ == "__main__":
    app.run(debug=True)
