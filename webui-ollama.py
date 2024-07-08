from flask import Flask, request, jsonify
from langchain_community.llms import Ollama
import subprocess

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
    # Başlatmadan önce ngrok'u çalıştırın
    ngrok_process = subprocess.Popen(["ngrok", "http", "5000"])
    app.run(debug=True)
    # ngrok'u kapatın
    ngrok_process.terminate()
