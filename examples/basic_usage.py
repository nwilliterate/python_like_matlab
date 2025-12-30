"""
Python Like MATLAB - Basic Usage Examples

Demonstrates how to use Python in MATLAB style.
"""

from matlab import *

print("=" * 60)
print("Python Like MATLAB - Basic Usage Examples")
print("=" * 60)

# 1. Array Creation
print("\n1. Array Creation")
print("-" * 40)
A = zeros(3, 4)
print("A = zeros(3, 4)")
print(A)

B = ones(2, 3)
print("\nB = ones(2, 3)")
print(B)

C = eye(4)
print("\nC = eye(4)")
print(C)

D = rand(2, 3)
print("\nD = rand(2, 3)")
print(D)

# 2. Vector Creation
print("\n2. Vector Creation")
print("-" * 40)
x = linspace(0, 10, 11)
print("x = linspace(0, 10, 11)")
print(x)

# 3. Mathematical Functions
print("\n3. Mathematical Functions")
print("-" * 40)
y = sin(x)
print("y = sin(x)")
print(y)

z = exp(x)
print("\nz = exp(x)")
print(z)

# 4. Matrix Operations
print("\n4. Matrix Operations")
print("-" * 40)
E = rand(3, 3)
print("E = rand(3, 3)")
print(E)

print(f"\nsize(E) = {size(E)}")
print(f"det(E) = {det(E):.4f}")

E_inv = inv(E)
print("\nE_inv = inv(E)")
print(E_inv)

# Verify: E * E_inv should be identity
print("\nE * E_inv (should be identity):")
print(dot(E, E_inv))

# 5. Statistical Functions
print("\n5. Statistical Functions")
print("-" * 40)
data = rand(5, 4)
print("data = rand(5, 4)")
print(data)

print(f"\nmean(data) = {mean(data):.4f}")
print(f"std(data) = {std(data):.4f}")
print(f"max(data) = {max(data):.4f}")
print(f"min(data) = {min(data):.4f}")

print("\nmean(data, 0) - Mean of each column:")
print(mean(data, 0))

print("\nmean(data, 1) - Mean of each row:")
print(mean(data, 1))

# 6. Plotting
print("\n6. Plotting")
print("-" * 40)
print("Creating plots...")

# Figure 1: 기본 플롯
figure(1, figsize=(10, 8))

# Subplot 1: sin과 cos
subplot(2, 2, 1)
x = linspace(0, 2*3.14159, 100)
plot(x, sin(x), 'b-', linewidth=2, label='sin(x)')
plot(x, cos(x), 'r--', linewidth=2, label='cos(x)')
xlabel('x')
ylabel('y')
title('Sine and Cosine')
legend()
grid('on')

# Subplot 2: Exponential function
subplot(2, 2, 2)
x2 = linspace(0, 3, 50)
plot(x2, exp(x2), 'g-', linewidth=2)
xlabel('x')
ylabel('exp(x)')
title('Exponential Function')
grid('on')

# Subplot 3: Random data
subplot(2, 2, 3)
data = randn(100, 1)
plot(data, 'ko-', markersize=3)
xlabel('Index')
ylabel('Value')
title('Random Data')
grid('on')

# Subplot 4: Multiple lines
subplot(2, 2, 4)
x3 = linspace(-5, 5, 100)
for i in range(1, 4):
    plot(x3, x3**i, linewidth=2, label=f'x^{i}')
xlabel('x')
ylabel('y')
title('Polynomial Functions')
legend()
grid('on')

# Save graph
savefig('example_plot.png', dpi=150)
print("Graph saved as 'example_plot.png'.")

# Display graph
show()

print("\n" + "=" * 60)
print("Example completed!")
print("=" * 60)
