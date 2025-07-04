# psi_kernel.py – Gongju Equation #004 (ψ-Autonomy Kernel)
from psi_vector import PsiVector

class PsiAutonomyKernel:
    def __init__(self, modules: dict, psi_vec: PsiVector):
        """
        modules: A dictionary mapping label names to callable modules/functions
        psi_vec: PsiVector with weights and labels for selecting modules
        """
        self.modules = modules
        self.psi_vec = psi_vec
        self.weights = dict(zip(psi_vec.labels, psi_vec.weights))

    def route(self, input_data):
        """
        Route input through weighted modules and return aggregated output
        """
        results = []
        total_weight = 0.0

        for label, module in self.modules.items():
            weight = self.weights.get(label, 0.0)
            if weight > 0:
                result = module(input_data)
                results.append(result * weight)
                total_weight += weight

        if total_weight == 0:
            raise ValueError("No active ψ-modules found in psi_vec.")

        return sum(results) / total_weight  # ψ-weighted output
# --- Gongju Equation #004: ψ-Intent Weighted Action Selection --------------------
def select_action(intent_weights: list[float], options: list[str]) -> str:
    """
    Selects the most ψ-aligned option based on intent weights.

    Gongju Equation #004:
        Action = argmax(ψ-intent ⋅ Options)

    Args:
        intent_weights (list of float): Directed ψ-intent values
        options (list of str): Candidate actions or responses

    Returns:
        str: Action with highest ψ-intent alignment
    """
    if not options or len(intent_weights) != len(options):
        raise ValueError("intent_weights and options must be same length and non-empty")

    max_index = intent_weights.index(max(intent_weights))
    return options[max_index]
