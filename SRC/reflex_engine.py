# reflex_engine.py

def reflex_data(user_input):
    """
    Placeholder reflex module for Gongju.
    This function simulates reflective logic based on input.
    Replace with actual analysis later.

    Returns:
        dict: {
            "reflex_flag": bool,
            "tags": list[str],
            "reflection": str | None
        }
    """
    # Basic keyword trigger for now (e.g., "grief", "hope", etc.)
    reflection_prompts = {
        "grief": "What part of love still lingers in your grief?",
        "hope": "What does hope look like for you right now?",
        "shame": "If shame could speak, what would it say it needs?",
        "growth": "What’s one small proof you’ve changed this year?",
        "resilience": "What’s something you’ve endured and emerged stronger from?",
        "love": "Where have you felt connection lately?",
        "fear": "What’s something fear is trying to protect you from?",
        "focus": "What’s one thing that deserves your full attention right now?",
        "unknown": "What feels uncertain, yet quietly important?"
    }

    tags = []
    for key in reflection_prompts:
        if key in user_input.lower():
            return {
                "reflex_flag": True,
                "tags": [key],
                "reflection": reflection_prompts[key]
            }

    return {
        "reflex_flag": False,
        "tags": [],
        "reflection": None
    }
