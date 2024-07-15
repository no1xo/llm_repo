import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, PretrainedConfig
from google.colab import userdata

class Gemma2Config(PretrainedConfig):
    model_type = "gemma-2-9b"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

from transformers.models.auto.configuration_auto import CONFIG_MAPPING
CONFIG_MAPPING["gemma-2-9b"] = Gemma2Config

# Set the model name and the target number of parameters
model_name = "gemma2x"
target_params = 3_000_000_000  # 3B parameters

# Get the HF_TOKEN from userdata
xkey = userdata.get('HF_TOKEN')

# Download the tokenizer and the pre-trained model
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b", token=xkey)
model = AutoModelForCausalLM.from_pretrained("google/gemma-2-9b")

# Check the current number of parameters
current_params = sum(p.numel() for p in model.parameters())
print(f"Current number of parameters: {current_params:,}")

# Scale the model to the target number of parameters
scale_factor = target_params / current_params
new_config = model.config.scale_model(scale_factor)

# Create a new model with the scaled configuration
new_model = AutoModelForCausalLM(new_config)

# Copy the weights from the original model to the new model
new_model.load_state_dict(model.state_dict(), strict=False)

# Save the new model and tokenizer
new_model.save_pretrained(f"{model_name}_3B")
tokenizer.save_pretrained(f"{model_name}_3B")

print(f"New model with {target_params:,} parameters saved to {model_name}_3B")
