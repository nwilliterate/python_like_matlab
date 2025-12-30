"""
Advanced Example: Linear Algebra
"""

from matlab import *

print("Advanced Example: Linear Algebra")
print("=" * 60)

# Matrix creation
print("\n1. Matrix Creation")
A = np.array([[4, 2, 1],
              [2, 5, 3],
              [1, 3, 6]])
print("A =")
print(A)

# Eigenvalues and Eigenvectors
print("\n2. Eigenvalue Decomposition")
eigenvalues, eigenvectors = eig(A)
print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)

# Singular Value Decomposition (SVD)
print("\n3. Singular Value Decomposition (SVD)")
U, S, Vh = svd(A)
print("U:")
print(U)
print("\nSingular values:")
print(S)
print("\nVh:")
print(Vh)

# Matrix inverse
print("\n4. Matrix Inverse")
A_inv = inv(A)
print("inv(A) =")
print(A_inv)

# Verification
print("\nA * inv(A) =")
print(dot(A, A_inv))

# Solve linear system: Ax = b
print("\n5. Solving Linear System (Ax = b)")
b = np.array([1, 2, 3])
x = np.linalg.solve(A, b)
print(f"b = {b}")
print(f"x = {x}")
print(f"Verification: A*x = {dot(A, x)}")

# Visualization: Eigenvectors
figure(figsize=(8, 8))
for i in range(3):
    v = eigenvectors[:, i]
    plot([0, v[0]], [0, v[1]], linewidth=3, label=f'Eigenvector {i+1}')

xlabel('x')
ylabel('y')
title('Eigenvectors')
legend()
grid('on')
xlim(-1.5, 1.5)
ylim(-1.5, 1.5)

savefig('eigenvectors.png', dpi=150)
print("\nGraph saved as 'eigenvectors.png'.")
show()
