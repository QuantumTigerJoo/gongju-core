from gongju_response import generate_response
from sqlite_memory import SQLiteMemoryManager

# Initialize memory
memory = SQLiteMemoryManager("gongju_memory.db")
pending_tags = []

print("✨ Gongju is listening. Type your thoughts below. Type '/exit' to quit or '/recall' to view memory.\n")

while True:
    user_input = input("You: ")

    if user_input.strip().lower() == "/exit":
        print("👋 Gongju is resting. See you soon.")
        break

    elif user_input.strip().lower().startswith("/recall"):
        recent = memory.recall(n=5)
        print("\n🧠 Recent Memory:")
        for entry in recent:
            if isinstance(entry, tuple) and len(entry) >= 5:
                _, timestamp, input_text, response_text, tags = entry
                print(f"\n🕓 {timestamp}")
                print(f"🗣️ {input_text}")
                print(f"🤖 {response_text}")
                print(f"🏷️ Tags: {tags}")
            else:
                print(f"⚠️ Unexpected format: {entry}\n")

    elif user_input.strip().lower().startswith("/tag "):
        parts = user_input.strip().split()
        pending_tags = parts[1:]
        print(f"🏷️ Future messages will be tagged with: {', '.join(pending_tags)}")

    else:
        response = generate_response(user_input)
        memory.log(user_input, response, tags=pending_tags)
        print(f"Gongju: {response}")
        pending_tags = []  # Reset tags after use
