!pip install --upgrade transformers
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GemmaConfig, CONFIG_MAPPING

# Register the 'gemma2' model type
CONFIG_MAPPING["gemma2"] = GemmaConfig

# Load the pre-trained tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b")
model_9b = AutoModelForCausalLM.from_pretrained("google/gemma-2-9b")

# Define a new configuration with a reduced number of hidden layers and hidden size
new_config = GemmaConfig.from_pretrained("google/gemma-2-9b", num_hidden_layers=12, hidden_size=1024)

# Create a new model with the new configuration
model_3b = AutoModelForCausalLM(new_config)

# Load the pre-trained weights into the new model, allowing for different layer counts and hidden sizes
model_3b.load_state_dict(model_9b.state_dict(), strict=False)

# Save the new model
new_model_path = "gemma_3b_model"
model_3b.save_pretrained(new_model_path)

print(f"New model with {new_config.num_hidden_layers} hidden layers and {new_config.hidden_size} hidden size created and saved to {new_model_path}.")
