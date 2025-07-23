# memory_reader.py

def load_triangle_reflections(filepath="gongju_memory_log.txt"):
    """
    Reads Gongju's symbolic memory file and returns a list of triangle-tagged reflection strings.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Only keep lines that contain triangle reflections (numbered lines)
        reflections = [
            line.strip() for line in lines
            if line.strip() and line.strip()[0].isdigit()
        ]
        return reflections

    except FileNotFoundError:
        return ["Memory log file not found."]
    except Exception as e:
        return [f"Error loading memory log: {e}"]
