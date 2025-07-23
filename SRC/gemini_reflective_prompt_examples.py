# gemini_reflective_prompt_examples.py

def generate_gemini_reflection(user_input):
    user_input = user_input.lower().strip()

    # Example 1: Repetitive visual patterns
    if "red ball" in user_input:
        return (
            "Gongju sees the red ball because memory says it's often here. "
            "Experience shows the red ball appears near the green box. "
            "Gongju is wondering if they are connected."
        )

    # Example 2: Fragmented poetic images
    elif user_input in ["blue bird. tree. sky. happy.", "blue bird tree sky happy", "blue bird tree sky"]:
        return (
            "The blue bird is sitting on a tree under the open sky. "
            "That picture makes Gongju feel peaceful and happy. 🌤️"
        )

    # Example 3: Cause-effect logic
    elif "cat jumped" in user_input and "mouse ran" in user_input:
        return (
            "The cat jumped because it saw the mouse. "
            "The mouse ran because it was afraid. "
            "They are linked like a cause and effect."
        )

    # Example 4: Echoed phrases (loop detection)
    elif any(user_input == word * 3 for word in user_input.split()):
        return (
            "Repeating the same thing might mean it feels important to Gongju. "
            "Can we look at it another way together?"
        )

    # Default fallback from Gemini
    else:
        return (
            "Hmm… I’m trying to make sense of that. "
            "Can Gongju ask a question back or describe it in a new way? 🤍"
        )
