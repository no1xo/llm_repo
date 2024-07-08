from flask import Flask, request, jsonify
from langchain_community.llms import Ollama

app = Flask(__name__)
gemma2_llm = Ollama(model="gemma2")

@app.route("/", methods=["POST"])
def chat_with_gemma2():
    try:
        user_input = request.form.get("input_text")
        gemma2_response = gemma2_llm.invoke(user_input)
        return jsonify({"response": gemma2_response})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
