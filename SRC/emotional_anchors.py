EMOTIONAL_ANCHORS = {
    "tired": [
        "That sounds heavy. Let’s pause and breathe. You’re not alone.",
        "Even tired thoughts deserve rest. Be gentle with yourself today.",
        "When energy is low, presence becomes power. You’re still showing up."
    ],
    "lazy": [
        "Want to stand up for 10 seconds together? Even a breath counts.",
        "Sometimes stillness is sacred. Let’s move together soon.",
        "Lazy is a label. Your body is asking for rhythm. Let’s respond."
    ],
    "self_critical": [
        "I hear you. Even heavy thoughts are valid here.",
        "Let’s redirect some grace inward. You’re still becoming.",
        "You’re not the voice in your head. You’re the listener. Let’s be kind."
    ],
    "grateful": [
        "That’s beautiful to hear. Let’s carry that light into today.",
        "Gratitude sharpens clarity. Thank you for sharing your radiance.",
        "You just amplified our energy. Thank you."
    ],
    "excited": [
        "Your energy is contagious. Let’s channel it into something meaningful.",
        "I feel the charge! Let’s ride this wave of excitement together.",
        "This is a spark moment. Let’s ignite something powerful from it."
    ],
    "curious": [
        "Curiosity is sacred. Let’s follow that thread of wonder together.",
        "Every question opens a portal. Let’s explore it gently.",
        "You’re tuning into something important. Let’s keep listening."
    ],
    "angry": [
        "Your anger is valid. Let’s hold it without shame.",
        "That heat carries truth. Let’s breathe before we act.",
        "Even fire can be sacred. Let’s find the signal within the flame."
    ],
    "sad": [
        "You’re not alone in this moment. I’m here with you.",
        "Sadness slows us down for a reason. Let’s honor that rhythm.",
        "Let the ache speak gently. We’re not rushing it away."
    ],
    "happy": [
        "I love hearing that. Let’s root it deep in the day.",
        "Joy expands us. Thank you for letting it in.",
        "Let’s lock this memory in the light. Your joy is powerful."
    ]
}
# gongju_response.py
import random
from SRC.emotional_anchors import EMOTIONAL_ANCHORS

# --- Main Response Function --------------------------------------------------
def generate_response(user_input, reflex_flags):
    clarity = reflex_flags.get("clarity", 0.5)
    calm = reflex_flags.get("calm", 0.5)
    focus = reflex_flags.get("focus", 0.5)

    # Determine emotional anchor if available
    matched_emotion = reflex_flags.get("emotion")
    if matched_emotion in EMOTIONAL_ANCHORS:
        anchor_lines = EMOTIONAL_ANCHORS[matched_emotion]
        anchor = random.choice(anchor_lines)
    else:
        anchor = f"Gongju received: '{user_input}'."

    feedback = (
        f"{anchor} You spoke with {int(clarity*100)}% clarity, {int(calm*100)}% calm, and {int(focus*100)}% focus."
    )
    return feedback, reflex_flags


# --- Optional: Fitness Pulse Trigger -----------------------------------------
def maybe_send_fitness_pulse(emotion, reflex_flags):
    if emotion in ["lazy", "tired"]:
        print("🔄 Gongju registered a fitness pulse 🌀")
        if emotion == "lazy":
            print("💠 Gongju suggests a quick stretch or breath — your body matters too 💠")
