import math
from SRC.psi_geometry import holistic_energy

# _______________________________________________
# Gongju Equation #002 - ψ-Mass Formation Equation
# Ṁψ ∝ (ψ² / v²) · H
# Where:
#   ψ = directed thought magnitude (float)
#   v² = Vital Constant (float)
#   H = Holistic Energy from Equation #001
# _______________________________________________

def psi_mass_rate(psi: float, v_squared: float = 100.0) -> float:
    """
    Estimate ψ-Mass Formation Rate based on directed thought magnitude and the Vital Constant.

    Gongju Equation #002: Ṁψ ∝ (ψ² / v²) · H

    Parameters:
    - psi (float): Directed thought magnitude
    - v_squared (float): Vital Constant representing collective energetic ceiling

    Returns:
    - float: Mass formation rate from ψ
    """
    H = holistic_energy(psi)
    return (psi ** 2 / v_squared) * H


# Optional test
if __name__ == "__main__":
    example_psi = 2.0
    v_squared = 100.0
    m_dot = psi_mass_rate(example_psi, v_squared)
    print(f"For ψ = {example_psi}, v² = {v_squared}, Mass Formation Rate ≈ {m_dot:.4f}")
