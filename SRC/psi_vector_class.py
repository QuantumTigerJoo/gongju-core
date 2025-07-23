class PsiVector:
    def __init__(self, weights, labels):
        assert len(weights) == len(labels), "Weights and labels must match"
        self.weights = weights
        self.labels = labels

    def get(self, label):
        if label in self.labels:
            return self.weights[self.labels.index(label)]
        else:
            raise ValueError(f"Label '{label}' not found.")

    def __repr__(self):  # ← This MUST be indented inside the class
        return f"PsiVector(weights={self.weights}, labels={self.labels})"
