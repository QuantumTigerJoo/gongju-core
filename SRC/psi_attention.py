# psi_attention.py
import torch
import numpy as np
import torch.nn as nn

from psi_vector import PsiVector

class PsiSparseAttention(nn.Module):
    def __init__(self, psi_vec: PsiVector, factor: float = 0.5):
        super().__init__()
        eff = psi_vec.get("efficiency")
        self.sparsity = float(np.clip(eff * factor, 0.0, 1.0))

    def forward(self, q, k, v):
        scores = torch.matmul(q, k.transpose(-2, -1)) / q.size(-1) ** 0.5
        if q.size(-2) > 3:
            threshold = torch.quantile(scores, self.sparsity)
            scores = torch.where(scores > threshold, scores, torch.finfo(scores.dtype).min)
        return torch.matmul(torch.softmax(scores, dim=-1), v)

# Optional test
if __name__ == "__main__":
    psi = PsiVector([0.9, 0.6], ["clarity", "efficiency"])
    layer = PsiSparseAttention(psi)

    # Dummy data (batch_size=1, seq_len=5, dim=4)
    qkv = torch.randn(1, 5, 4)
    out = layer(qkv, qkv, qkv)
    print("Output:", out)
