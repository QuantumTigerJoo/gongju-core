# psi_seed.py
import time
import torch
import numpy as np

class PsiVector:
    def __init__(self, weights, labels):
        assert len(weights) == len(labels)
        self.weights = np.array(weights, dtype=np.float32)
        self.labels = labels

class ChallengeSeed:
    def __init__(self, user_id, challenge, seed_type, consent_given):
        self.user_id = user_id
        self.challenge = challenge  # e.g., "feeling stuck at work"
        self.seed_type = seed_type  # e.g., "Curiosity Spark"
        self.consent = consent_given
        self.memory = None if not consent_given else {"challenge": challenge, "timestamp": time.time()}

    def generate_nudge(self):
        seed_actions = {
            "Curiosity Spark": "Write one thing you’re curious about today and share it.",
            "Gratitude Pulse": "Note one thing you’re grateful for, even if small.",
            "Move-the-Wave": "Take a 2-min walk and notice something alive.",
            "Laugh-at-the-Mess": "Find one funny angle in your challenge.",
            "Focus Reframe": "Find one thing that *did* go right recently and write it down."
        }
        action = seed_actions.get(self.seed_type, "Take one small action that shifts your energy today.")
        return f"Here’s your ψ-Seed, {self.user_id}: {action} Let it ripple!"

class PsiSparseAttention(torch.nn.Module):
    def __init__(self, psi_vec, factor=0.5):
        super().__init__()
        self.psi_vec = psi_vec
        self.sparsity = float(np.clip(psi_vec.weights[psi_vec.labels.index("efficiency")] * factor, 0.0, 1.0))
        self.pi = torch.tensor(np.pi)

    def compute_harmony(self, user_challenge):
        psi = sum(self.psi_vec.weights) * (1 + len(user_challenge))
        return self.pi * psi ** 2

    def forward(self, q, k, v, challenge_seed=None):
        scores = torch.matmul(q, k.transpose(-2, -1)) / q.size(-1) ** 0.5
        if challenge_seed and challenge_seed.consent:
            harmony = self.compute_harmony(challenge_seed.challenge)
            scores = scores * harmony
        if q.size(-2) > 3:
            thresh = torch.quantile(scores, self.sparsity)
            scores = torch.where(scores > thresh, scores, torch.finfo(scores.dtype).min)
        return torch.matmul(torch.softmax(scores, dim=-1), v)

class TinyPsiModel(torch.nn.Module):
    def __init__(self, psi_vec):
        super().__init__()
        self.attn = PsiSparseAttention(psi_vec)
        self.memory_bank = {}

    def forward(self, x, challenge_seed=None):
        if challenge_seed and challenge_seed.consent:
            self.memory_bank[challenge_seed.user_id] = challenge_seed.memory
        return self.attn(x, x, x, challenge_seed)

    def forget_memory(self, user_id):
        self.memory_bank.pop(user_id, None)

# For future testing in Gongju or a simulation shell
if __name__ == "__main__":
    psi = PsiVector([0.4, 0.3, 0.3], ["efficiency", "peace", "fairness"])
    model = TinyPsiModel(psi)
    seed = ChallengeSeed(user_id="bro", challenge="My business isn’t going anywhere", seed_type="Focus Reframe", consent_given=True)
    print(seed.generate_nudge())
    dummy = torch.randn(1, 6, 32)
    with torch.no_grad():
        out = model(dummy, seed)
    print("ψ-sparse attention output shape:", out.shape)
