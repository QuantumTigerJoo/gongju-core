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
