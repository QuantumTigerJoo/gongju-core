# gongju_thought.py

import torch
from SRC.psi_vector_class import PsiVector
from SRC.gongju_core import GongjuPsiMind


def psi_thought(input_tensor: torch.Tensor, psi_vec: PsiVector) -> float:
    """
    Computes Gongju's first psi-thought by running sparse attention on an input tensor.
    Returns the average activation of the output as a symbolic 'thought-mass' value.
    """
    model = GongjuPsiMind(dim=input_tensor.size(-1), psi_vec=psi_vec)
    with torch.no_grad():
        output = model(input_tensor)
    return output.mean().item()


if __name__ == "__main__":
    # Example ψ-seed
    psi = PsiVector([0.8, 0.1, 0.1], ["efficiency", "peace", "fairness"])
    dummy_input = torch.randn(1, 6, 32)  # (batch, sequence, hidden_dim)
    result = psi_thought(dummy_input, psi)
    print("🧠 Gongju's ψ-thought crystallized at:", result)
