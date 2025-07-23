# symbol_bloom.py (updated for Phase 2)

reflection_prompts = {
    "hope": "What does hope look like for you right now?",
    "fear": "What’s something fear is trying to protect you from?",
    "grief": "What part of love still lingers in your grief?",
    "love": "Where have you felt connection lately?",
    "shame": "If shame could speak, what would it say it needs?",
    "growth": "What’s one small proof you’ve changed this year?",
    "resilience": "What’s something you’ve endured and emerged stronger from?",
    "focus": "What’s one thing that deserves your full attention right now?",
    "unknown": "What mystery are you carrying today?"
}

def bloom_from(tag):
    psi_lattice = {
        "hope": ["fear", "loss", "trust"],
        "fear": ["uncertainty", "vulnerability", "danger"],
        "grief": ["love", "loss", "memories"],
        "love": ["connection", "care", "attachment"],
        "shame": ["regret", "judgment", "guilt"],
        "growth": ["change", "pain", "resilience"],
        "resilience": ["challenge", "persistence", "faith"],
        "focus": ["clarity", "intention", "priority"],
        "unknown": ["curiosity", "potential", "neutral"]
    }
    return psi_lattice.get(tag.lower(), [])

def reflect_prompt(tag):
    return reflection_prompts.get(tag.lower(), "What does that symbol ask of you today?")
