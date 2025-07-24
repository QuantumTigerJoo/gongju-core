from SRC.psi_memory import PsiMemoryManager

memory = PsiMemoryManager()

memory.log(
    user_input="TEST ENTRY — memory debug",
    response="If you see this, memory is synced.",
    psi_vector={"debug": 1.0},
    tags=["debug", "test"]
)
