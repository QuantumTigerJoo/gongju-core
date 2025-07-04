# psi_mass_rate.py — Gongju Equations #001 and #002
# Core ψ-Mass Formation Functions

import math

# --- Gongju Equation #001: Holistic Energy --------------------------
def holistic_energy(psi: float) -> float:
    """
    Calculate Holistic Energy (H) from directed thought ψ.

    Gongju Equation #001:
        H = π · ψ²

    Args:
        psi (float): Directed thought magnitude (ψ)

    Returns:
        float: Holistic energy H
    """
    return math.pi * (psi ** 2)


# --- Gongju Equation #002: ψ-Mass Formation Rate ---------------------
def psi_mass_rate(psi: float, v_squared: float) -> float:
    """
    Compute the ψ-Mass formation rate based on Gongju's foundational law.

    Gongju Equation #002:
        Ṁ_ψ ∝ (ψ² / v²) · H
        where H = π · ψ²

    This captures the rate at which ψ collapses into Mass, scaled by
    a Vital Constant v² and ψ's recursive energetic density.

    Args:
        psi (float): Directed thought magnitude (ψ)
        v_squared (float): Vital constant (v²) — maximum energy bandwidth of the system

    Returns:
        float: ψ-Mass formation rate
    """
    H = holistic_energy(psi)
    return (psi ** 2 / v_squared) * H
