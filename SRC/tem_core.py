# tem_core.py

from collections import Counter
from psi_memory import PsiMemoryManager

def extract_symbol_field(n=20):
    """
    Analyze the last n memory entries and extract dominant ψ-symbol patterns.
    Returns a dict with dominant tag and frequency spectrum.
    """
    memory = PsiMemoryManager()
    entries = memory.recall(n=n)
    all_tags = []

    for entry in entries:
        tags = entry.get("tags", [])
        # Exclude compression-only entries
        filtered = [t for t in tags if t != "compression"]
        all_tags.extend(filtered)

    if not all_tags:
        return {
            "dominant": None,
            "spectrum": [],
            "summary": "Gongju hasn’t seen enough of your heart yet. Let’s keep going."
        }

    count = Counter(all_tags)
    most_common = count.most_common(3)
    dominant = most_common[0][0]
    spectrum_str = " / ".join([f"{tag} ({freq})" for tag, freq in most_common])

    return {
        "dominant": dominant,
        "spectrum": most_common,
        "summary": f"🧭 Gongju sees a ψ-field centered on *{dominant}* → {spectrum_str}"
    }
