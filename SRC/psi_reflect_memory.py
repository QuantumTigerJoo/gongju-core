import random

REFLECTION_PROMPTS = {
    "hope": "What does hope look like for you right now?",
    "fear": "What’s something fear is trying to protect you from?",
    "grief": "What part of love still lingers in your grief?",
    "love": "Where have you felt connection lately?",
    "shame": "If shame could speak, what would it say it needs?",
    "growth": "What’s one small proof you’ve changed this year?",
    "resilience": "What’s something you’ve endured and emerged stronger from?",
    "focus": "What’s one thing that deserves your full attention right now?",
    "unknown": "What might be forming that you can’t yet name?",
    "rebellion": "What truth have you outgrown that others still cling to?",
    "forgiveness": "What weight would lift if you forgave yourself?",
    "rejection": "What part of you still believes you're unworthy?",
    "faith": "What keeps you moving when proof is missing?",
    "joy": "Where has light broken through lately?"
}

class PsiReflector:
    def generate_prompt(self, topic):
        return REFLECTION_PROMPTS.get(topic, f"What does {topic} mean to you right now?")


    def reflect_on_tag(self, tag):
        return self.prompts.get(tag, "What’s forming beneath the surface of your thoughts?")
