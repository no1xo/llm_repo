import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Gemma 2 9B modelini yükleyin
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2-9b", device_map="auto", torch_dtype=torch.bfloat16)


# Modeli kesin ve sıkıştırın
converter = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)
quantized_model = converter.to("cpu")

# Kesilmiş ve sıkıştırılmış modeli kaydedin
quantized_model.save_pretrained("gemma2_3b_model")
tokenizer.save_pretrained("gemma2_3b_model")

print("Kesilmiş ve sıkıştırılmış model kaydedildi: gemma2_3b_model")
