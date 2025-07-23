from psi_kernel import PsiAutonomyKernel
from psi_vector_class import PsiVector







# Define a simple ψ-vector with directed intent weights
psi_vec = PsiVector(
    weights=[0.85, 0.1, 0.4],
    labels=["encourage", "pause", "humor"]
)

# Define sample module functions
def encourage(x): return "Keep pushing — you're doing amazing!"
def pause(x):     return "Let’s pause and breathe for a second."
def humor(x):     return "Why don’t we train our brain with some dumbbell jokes?"

# Map modules to labels
modules = {
    "encourage": encourage,
    "pause": pause,
    "humor": humor
}

# Initialize the ψ-kernel
kernel = PsiAutonomyKernel(modules=modules, psi_vec=psi_vec)

# Route a dummy input
result = kernel.route("dummy_input")

# Output the response
print("🔊 Gongju Response:", result)
