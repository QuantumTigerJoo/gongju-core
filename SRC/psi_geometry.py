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

def calculate_H(psi: float) -> float:
    """
    Compatibility wrapper for holistic_energy.
    Used by Gongju App for clarity.
    """
    return holistic_energy(psi)

def calculate_mass_rate(psi: float, v: float) -> float:
    """
    Calculate mass formation rate from ψ and Vital Constant v².

    Equation:
        Ṁψ ∝ (ψ² / v²) · H
    where H = π · ψ²

    Parameters:
    - psi (float): Directed thought value
    - v (float): Vital constant

    Returns:
    - float: Mass formation rate
    """
    H = calculate_H(psi)
    return (psi ** 2 / v ** 2) * H

# ─────────────────────────────────────────────
# Optional Test
# ─────────────────────────────────────────────

if __name__ == "__main__":
    example_psi = 2.0
    example_v = 10.0
    H = calculate_H(example_psi)
    M = calculate_mass_rate(example_psi, example_v)
