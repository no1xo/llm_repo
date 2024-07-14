
import torch
from torch import nn
import asyncio
from transformers import RagTokenizer, RagModel
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory


class GEMMA2B_RAG_3B(nn.Module):
    def __init__(self, num_genes, num_samples, latent_dim=128, hidden_dim=256):
        super(GEMMA2B_RAG_3B, self).__init__()
        self.num_genes = num_genes
        self.num_samples = num_samples
        self.latent_dim = latent_dim
        self.hidden_dim = hidden_dim

        # RAG model
        self.rag_model = RagModel.from_pretrained("facebook/rag-token-base")
        self.rag_tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")

        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, latent_dim)
        )

        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_genes * num_samples)
        )

    def forward(self, X):
        # Matrix tokenization
        X = X.view(X.size(0), -1)

        # RAG representation
        rag_input = self.rag_tokenizer(X, return_tensors="pt")
        rag_output = self.rag_model(**rag_input)
        rag_representation = rag_output.hidden_states[-1][:, 0, :]

        # Encoding
        Z = self.encoder(rag_representation)

        # Decoding
        X_hat = self.decoder(Z)

        # Matrix to vectors
        X_hat = X_hat.view(X.size(0), self.num_genes, self.num_samples)

        return X_hat


async def chat_with_model_async(model, tokenizer):
    while True:
        # Get user input
        user_input = await prompt(
            ">> ",
            history=FileHistory("chat_history.txt"),
            auto_suggest=AutoSuggestFromHistory(),
        )

        if user_input.strip() == "quit":
            break

        # Prepare the input
        input_ids = tokenizer.encode(user_input, return_tensors="pt")

        # Run the model
        with torch.no_grad():
            output = model(input_ids)

        # Decode the output
        output_ids = torch.argmax(output, dim=2)
        decoded_output = tokenizer.decode(output_ids[0])

        # Print the response
        print(f"Model: {decoded_output}")


def chat_with_model(model, tokenizer):

    loop = asyncio.get_event_loop()
    if not loop.is_running():
        loop.run_until_complete(chat_with_model_async(model, tokenizer))
    else:
        print("The event loop is already running. Please stop it first.")

if __name__ == "__main__":
    # Load the model and tokenizer
    model = GEMMA2B_RAG_3B(num_genes=1000, num_samples=1)  # Adjust num_genes as needed
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base")

    # Start the chat CLI
    chat_with_model(model, tokenizer)