# pattern_logic.py

def tag_psi_symbol(user_input):
    """
    Analyze user input and return a symbolic ψ-tag based on mood or theme.
    Combines keyword spotting and primitive semantic matching.
    """
    input_lower = user_input.lower()

    # Simple keyword groupings for emotional-symbolic tags
    tag_keywords = {
        "hope": ["hope", "faith", "believe", "trust", "possibility", "potential"],
        "fear": ["fear", "anxious", "worried", "afraid", "panic", "doubt"],
        "grief": ["loss", "sad", "grieve", "mourning", "alone", "gone"],
        "focus": ["goal", "focus", "clarity", "plan", "target", "next step"],
        "resilience": ["strong", "endure", "persist", "keep going", "survive"],
        "shame": ["ashamed", "regret", "guilt", "embarrassed", "not enough"],
        "growth": ["learn", "growth", "change", "transform", "evolve", "adapt"],
        "love": ["love", "connection", "care", "compassion", "bond", "relationship"],
    }

    detected_tags = []

    for tag, keywords in tag_keywords.items():
        if any(word in input_lower for word in keywords):
            detected_tags.append(tag)

    # Fallback default
    if not detected_tags:
        detected_tags.append("unknown")

    return detected_tags
