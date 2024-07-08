from langchain_community.llms import Ollama

# Gemma 2 modelini yükle
gemma2_llm = Ollama(model="gemma2")

# Llama 3 modelini yükle (örnek olarak)
llama3_llm = Ollama(model="llama3")

# Kullanıcıdan soru al
while True:
    user_question = input("Soru: ")
    
    # Gemma 2'den cevap al
    gemma2_answer = gemma2_llm.invoke(user_question)
    print(f"Gemma 2: {gemma2_answer}")
    
    # Llama 3'ten cevap al
    llama3_answer = llama3_llm.invoke(user_question)
    print(f"Llama 3: {llama3_answer}")
