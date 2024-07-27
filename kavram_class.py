import re
import numpy as np
import pandas as pd
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Kavramlar arası ilişki matrisini oluşturun
data = {
    'Eylem': [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    'Özne': [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    'Nesne': [1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    'Aksiyon': [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    'Durum': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    'Konu': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    'Canlı': [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    'Cansız': [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    'Fiziksel Eylem': [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    'Zihinsel Eylem': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    'Zaman': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    'Yer': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    'Koşul': [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
    'Tema': [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1]
}

# Kavramları ve matrisini DataFrame olarak oluşturun
df = pd.DataFrame(data, index=['Eylem', 'Özne', 'Nesne', 'Aksiyon', 'Durum', 'Konu', 'Canlı', 'Cansız', 'Fiziksel Eylem', 'Zihinsel Eylem', 'Zaman', 'Yer', 'Koşul', 'Tema'])

def clean_text(text):
    """Yazıdan kelimeleri temizler ve küçük harfe çevirir."""
    return re.sub(r'\W+', ' ', text).lower()

def create_vectorizer(corpus):
    """TF-IDF vektörizer oluşturur."""
    vectorizer = TfidfVectorizer()
    vectorizer.fit(corpus)
    return vectorizer

def classify_text(text, concept_matrix):
    """Metni kavram matrisine göre sınıflandırır."""
    # Cümleleri temizle
    sentences = [clean_text(s) for s in re.split(r'\.\s*', text) if s.strip()]
    
    # Kavram etiketlerini hazırlayın
    concept_labels = concept_matrix.columns.tolist()
    
    # Cümleleri ve kavramları vektörize et
    vectorizer = create_vectorizer(sentences + concept_labels)
    sentence_vectors = vectorizer.transform(sentences)
    concept_vectors = vectorizer.transform(concept_labels)
    
    # Benzerlikleri hesapla
    similarities = cosine_similarity(sentence_vectors, concept_vectors)
    
    # Benzerlik eşiği
    similarity_threshold = 0.1
    
    classification = defaultdict(list)
    
    for i, sentence in enumerate(sentences):
        max_similarities = similarities[i]
        relevant_concepts = [concept_labels[j] for j, similarity in enumerate(max_similarities) if similarity > similarity_threshold]
        classification[sentence] = relevant_concepts
    
    return classification

def chat_bot():
    print("Chatbot: Merhaba! Size nasıl yardımcı olabilirim? (Çıkmak için 'quit' yazın)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Görüşürüz!")
            break
        
        # Kullanıcıdan gelen metni sınıflandır
        classification_result = classify_text(user_input, df)
        
        # Sonuçları formatla
        response = []
        for sentence, concepts in classification_result.items():
            if concepts:
                concept_labels = ', '.join(concepts)
                response.append(f'"{sentence}" - Kavramlar: {concept_labels}')
    
        if not response:
            response = ["Bu metinle ilgili kavram bulamadım."]
        
        print("Chatbot:", " | ".join(response))

if __name__ == "__main__":
    chat_bot()
