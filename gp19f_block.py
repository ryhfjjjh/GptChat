import torch
import torch.nn as nn
import torch.nn.functional as F

class GP19FBlock(nn.Module):
    def __init__(self, vocab_size=10000, max_len=612, embedding_dim=802, num_layers=17):
        super(GP19FBlock, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.positional_encoding = nn.Parameter(torch.zeros(1, max_len, embedding_dim))
        self.transformer_layers = nn.ModuleList([
            nn.TransformerEncoderLayer(d_model=embedding_dim, nhead=8, dim_feedforward=2048, dropout=0.1, activation='gelu')
            for _ in range(num_layers)
        ])
        self.attention_weights = nn.Linear(embedding_dim, 1)
        self.fc_out = nn.Linear(embedding_dim, vocab_size)
        self.context_memory = []

    def forward(self, x):
        embed = self.embedding(x) + self.positional_encoding[:, :x.size(1), :]
        
        # Адаптивті attention
        for layer in self.transformer_layers:
            embed = layer(embed)

        # Контекст жады сақтау (соңғы репрезентацияны есте сақтау)
        self.context_memory.append(embed.detach())
        if len(self.context_memory) > 5:
            self.context_memory.pop(0)

        logits = self.fc_out(embed)
        return logits

    def get_response_time(self, num_words: int, complexity: str) -> float:
        if num_words <= 15:
            input_time = 3
        elif num_words <= 30:
            input_time = 6
        else:
            input_time = 10

        complexity_map = {
            'easy': 2,
            'medium': 5,
            'hard': 8,
            'complex': 11
        }

        think_time = complexity_map.get(complexity.lower(), 5)
        return input_time + think_timdef
    gp19f_answer(name):
    # Бұл жерде GP19F жүйесі нақтылайды
    return f"Бұл адамның аты — {name}. Қате жоқ."
