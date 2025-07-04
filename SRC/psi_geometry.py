import math

# ─────────────────────────────────────────────
# Gongju Equation #001 – Holistic Energy Equation
# H = π · ψ²
# Where:
#   ψ (psi) = directed thought magnitude (float)
#   H       = holistic energy (float)
#   π       = mathematical constant (math.pi)
# ─────────────────────────────────────────────

def holistic_energy(psi: float) -> float:
    """
    Calculate Holistic Energy (H) from a given ψ (directed thought).
    Gongju Equation #001: H = π · ψ²

    Parameters:
    - psi (float): Directed thought magnitude

    Returns:
    - float: Holistic energy output
    """
    return math.pi * (psi ** 2)

# Optional test
if __name__ == "__main__":
    example_psi = 2.0
    print(f"For ψ = {example_psi}, Holistic Energy (H) = {holistic_energy(example_psi):.4f}")
