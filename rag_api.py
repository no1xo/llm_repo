import requests                                            
from langchain.chains import RetrievalQA                   
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings          
from langchain.vectorstores import FAISS                   
from langchain.llms import LlamaCpp
# API URL'sini belirtin
api_url = "https://api.example.com/data"
# Verileri çekmek için bir fonksiyon oluşturun
def get_updated_data():                                     
	response = requests.get(api_url)                           
	if response.status_code == 200:                              
		return response.json()                                   
	else:
	 print("API bağlantısı hatası!")
	return None
# Verileri yükleyin ve embeddings oluşturun
documents = get_updated_data()
embeddings = OpenAIEmbeddings()                            
vectorstore = FAISS.from_documents(documents,embeddings)
# Llama 3 modeli yükleyin                                  
llm = LlamaCpp(model_path="your_llama_3_model_path")
# RAG uygulamasını oluşturun                               
qa=RetrievalQA.from_chain.type( 
llm=llm,retriever=vectorstore.as_retriever(),                    return_source_documents=True )
# Soru sorun ve yanıt alın
query = "Soru sorunuz burada"
answer = qa.run(query)
print(answer)

# Verileri düzenli aralıklarla güncelleyin (örneğin,
her 10 dakikada bir)
while True:
  documents = get_updated_data()
  vectorstore.update_documents(documents)
  time.sleep(600)  # 10 dakika bekle