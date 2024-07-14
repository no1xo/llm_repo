
# Gerekli kütüphaneleri yükleyin
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Model ve tokenizer'ı yükle (Örneğin, Gemma 2B)
model_name = "google/gemma-2b"  
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 1. Parametre Sayısını Azaltma: Katmanları Kaldırma Örneği

# Modelin son birkaç katmanını kaldıralım (bu, performansı etkileyebilir).
for i in range(-3, 0): # Son 3 katmanı kaldırmak için 
    del model.encoder.layer[i]  

# 2. Modeli İnce Ayarlamaya Hazırlama

# Örnek veri seti (örneğimiz için sadece birkaç cümle)
training_data = [
    "Bu güzel bir gün.",
    "Bugün hava sıcak.",
    "Parkta yürümek istiyorum.",
]
 
# Tokenize edip modelin anlayabileceği hale getir
input_ids = tokenizer(training_data, padding=True, truncation=True, return_tensors="pt")

# Eğitim için gereken ayarları yapın

optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5) 

epochs = 3 # Eğitilecek döngü sayısı (sınırlı kaynaklar nedeniyle düşük tutun)


# İnce Ayarlama Döngüsü

for epoch in range(epochs):
    optimizer.zero_grad() # Gradyanları sıfırlayın
    outputs = model(**input_ids) 
    loss = outputs.loss # Modeli kaybını hesaplayın
    loss.backward()  # Geriye doğru yayılım ile gradyanları hesaplayın
    optimizer.step()  # Parametreleri güncelleyin

# Modelin kayıt edilmesi

model.save_pretrained("my_finetuned_gemma")
