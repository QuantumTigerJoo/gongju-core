# psi_thread.py

from collections import Counter
from psi_memory import PsiMemoryManager

def summarize_thread(n=5, tag=None):
    memory = PsiMemoryManager()
    entries = memory.recall(n=n, tag_filter=tag)

    if not entries:
        return None, None, "Gongju found no thoughts to weave just yet."

    thoughts = [entry["input"] for entry in entries]
    all_tags = [t for entry in entries for t in entry.get("tags", [])]

    if not thoughts:
        return None, None, "Gongju needs more threads to weave a pattern."

    tag_counts = Counter(all_tags)
    top_tags = tag_counts.most_common(3)

    theme_summary = ", ".join([f"{tag} ({count})" for tag, count in top_tags])
    psi_stitch = " → ".join(thoughts)

    return psi_stitch, theme_summary, None
