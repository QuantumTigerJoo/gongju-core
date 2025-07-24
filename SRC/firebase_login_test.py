from SRC.firebase_memory import FirebaseMemoryManager

memory_manager = FirebaseMemoryManager()
user_id = "Joosace"
password = "sunflower88"

if memory_manager.login(user_id, password):
    print("✅ Login successful!")
else:
    print("❌ Login failed.")
