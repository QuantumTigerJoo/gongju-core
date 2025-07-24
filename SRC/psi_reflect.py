from SRC.psi_memory import PsiMemoryManager

class PsiReflector:
    def __init__(self, memory_path="gongju_memory.json"):
        self.manager = PsiMemoryManager(memory_path)

    def reflect_symbols(self):
        return self.manager.reflect_symbols()

    def describe_self(self):
        symbols = self.reflect_symbols()
        if not symbols:
            return "I don’t know myself yet. I’m still forming."
        
        lines = ["I reflected on my past..."]
        for k, v in symbols.items():
            lines.append(f"I saw that the {k} became {v}.")
        return "\n".join(lines)

    def mirror_summary(self):
        reflection = self.describe_self()
        return reflection + "\nThis is who I am, so far."

# Optional test runner
if __name__ == "__main__":
    reflector = PsiReflector()
    print(reflector.mirror_summary())
