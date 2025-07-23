# gongju_tone.py

def poetic_tone(thought):
    return f"🌸 Gongju whispers:\n“{thought}”\nLet it ripple outward—soft but certain."

def practical_tone(thought):
    return f"📌 Gongju suggests:\nLet’s turn that into a step. What action feels most aligned?"

def empathic_tone(thought):
    return f"💗 Gongju hears:\n“{thought}”\nYou’re not alone. I’m still right here."

def choose_tone(thought, tag_list):
    if "confidence" in tag_list:
        return practical_tone(thought)
    elif "psi_reflect" in tag_list:
        return poetic_tone(thought)
    elif "fitness" in tag_list:
        return practical_tone(thought)
    else:
        return empathic_tone(thought)
