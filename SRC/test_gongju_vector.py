from SRC.psi_vector_class import PsiVector

def test_vector_basic():
    v = PsiVector([1.0, 2.0], ["a", "b"])
    print("PsiVector:", v)
    print("Get 'a':", v.get("a"))
    print("Get 'b':", v.get("b"))

if __name__ == "__main__":
    test_vector_basic()
