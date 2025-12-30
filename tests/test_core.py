"""
Python Like MATLAB Tests
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from matlab import *
import numpy as np


def test_array_creation():
    """Test array creation functions"""
    print("Testing array creation...")
    
    # zeros
    A = zeros(3, 4)
    assert A.shape == (3, 4)
    assert np.all(A == 0)
    
    # ones
    B = ones(2, 3)
    assert B.shape == (2, 3)
    assert np.all(B == 1)
    
    # eye
    I = eye(3)
    assert I.shape == (3, 3)
    assert np.allclose(I, np.eye(3))
    
    # linspace
    x = linspace(0, 10, 11)
    assert len(x) == 11
    assert x[0] == 0
    assert x[-1] == 10
    
    print("✓ Array creation tests passed!")


def test_matrix_operations():
    """Test matrix operations"""
    print("Testing matrix operations...")
    
    A = rand(3, 3)
    
    # size
    s = size(A)
    assert s == (3, 3)
    assert size(A, 0) == 3
    assert size(A, 1) == 3
    
    # length
    assert length(A) == 3
    
    # transpose
    At = transpose(A)
    assert At.shape == (3, 3)
    
    # inv and det
    if abs(det(A)) > 0.01:  # Only when matrix has inverse
        A_inv = inv(A)
        identity = dot(A, A_inv)
        assert np.allclose(identity, np.eye(3), atol=1e-10)
    
    print("✓ Matrix operation tests passed!")


def test_statistics():
    """Test statistics functions"""
    print("Testing statistics functions...")
    
    # Test with known data
    data = np.array([[1, 2, 3],
                     [4, 5, 6]])
    
    # mean
    m = mean(data)
    assert m == 3.5
    
    m_col = mean(data, 0)
    assert np.allclose(m_col, [2.5, 3.5, 4.5])
    
    m_row = mean(data, 1)
    assert np.allclose(m_row, [2, 5])
    
    # sum
    s = sum(data)
    assert s == 21
    
    # max and min
    assert max(data) == 6
    assert min(data) == 1
    
    print("✓ Statistics tests passed!")


def test_math_functions():
    """Test math functions"""
    print("Testing math functions...")
    
    x = linspace(0, 2*np.pi, 100)
    
    # sin, cos
    y1 = sin(x)
    y2 = cos(x)
    
    # sin^2 + cos^2 = 1 verification
    assert np.allclose(y1**2 + y2**2, 1)
    
    # exp and log
    x2 = linspace(1, 10, 50)
    y3 = exp(log(x2))
    assert np.allclose(y3, x2)
    
    print("✓ Math function tests passed!")


def test_linear_algebra():
    """Test linear algebra functions"""
    print("Testing linear algebra functions...")
    
    # Create symmetric matrix (eigenvalues are real)
    A = rand(3, 3)
    A = A + transpose(A)  # Symmetric matrix
    
    # Eigenvalue decomposition
    eigenvalues, eigenvectors = eig(A)
    assert len(eigenvalues) == 3
    assert eigenvectors.shape == (3, 3)
    
    # SVD
    U, S, Vh = svd(A)
    assert U.shape == (3, 3)
    assert len(S) == 3
    assert Vh.shape == (3, 3)
    
    # Reconstruction verification
    A_reconstructed = dot(U * S, Vh)
    assert np.allclose(A, A_reconstructed)
    
    print("✓ Linear algebra tests passed!")


if __name__ == '__main__':
    print("=" * 60)
    print("Running Python Like MATLAB Tests")
    print("=" * 60)
    print()
    
    try:
        test_array_creation()
        test_matrix_operations()
        test_statistics()
        test_math_functions()
        test_linear_algebra()
        
        print()
        print("=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
    except AssertionError as e:
        print()
        print("=" * 60)
        print("✗ Test failed!")
        print(f"Error: {e}")
        print("=" * 60)
        sys.exit(1)
