"""
MATLAB-style matrix operation functions
"""

import numpy as np
from typing import Union, Tuple


def size(A: np.ndarray, dim: Union[int, None] = None) -> Union[Tuple[int, ...], int]:
    """
    Return the size of an array
    
    Parameters:
    -----------
    A : ndarray
        Input array
    dim : int, optional
        Specific dimension (if omitted All dimensions)
    
    Returns:
    --------
    tuple or int
        Array size
    
    Examples:
    ---------
    >>> A = zeros(3, 4)
    >>> size(A)  # (3, 4)
    >>> size(A, 0)  # 3
    >>> size(A, 1)  # 4
    """
    if dim is None:
        return A.shape
    return A.shape[dim]


def length(A: np.ndarray) -> int:
    """
    Return the length of the largest dimension
    
    Parameters:
    -----------
    A : ndarray
        Input array
    
    Returns:
    --------
    int
        Size of the largest dimension
    
    Examples:
    ---------
    >>> A = zeros(3, 4)
    >>> length(A)  # 4
    """
    return max(A.shape) if A.shape else 0


def reshape(A: np.ndarray, m: int, n: int) -> np.ndarray:
    """
    Reshape an array
    
    Parameters:
    -----------
    A : ndarray
        Input array
    m : int
        New number of rows
    n : int
        New number of columns
    
    Returns:
    --------
    ndarray
        Reshaped array
    
    Examples:
    ---------
    >>> A = rand(12, 1)
    >>> B = reshape(A, 3, 4)
    """
    return np.reshape(A, (m, n))


def transpose(A: np.ndarray) -> np.ndarray:
    """
    Transpose an array
    
    Parameters:
    -----------
    A : ndarray
        Input array
    
    Returns:
    --------
    ndarray
        Transposed array
    
    Examples:
    ---------
    >>> A = rand(3, 4)
    >>> B = transpose(A)
    """
    return np.transpose(A)


def inv(A: np.ndarray) -> np.ndarray:
    """
    Calculate inverse matrix
    
    Parameters:
    -----------
    A : ndarray
        Input square matrix
    
    Returns:
    --------
    ndarray
        Inverse matrix
    
    Examples:
    ---------
    >>> A = rand(3, 3)
    >>> B = inv(A)
    """
    return np.linalg.inv(A)


def det(A: np.ndarray) -> float:
    """
    Calculate determinant
    
    Parameters:
    -----------
    A : ndarray
        Input square matrix
    
    Returns:
    --------
    float
        Determinant value
    
    Examples:
    ---------
    >>> A = rand(3, 3)
    >>> d = det(A)
    """
    return np.linalg.det(A)


def eig(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calculate eigenvalues and eigenvectors
    
    Parameters:
    -----------
    A : ndarray
        Input square matrix
    
    Returns:
    --------
    eigenvalues : ndarray
        Eigenvalues
    eigenvectors : ndarray
        Eigenvectors
    
    Examples:
    ---------
    >>> A = rand(3, 3)
    >>> eigenvalues, eigenvectors = eig(A)
    """
    return np.linalg.eig(A)


def svd(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Singular Value Decomposition (SVD) (SVD)
    
    Parameters:
    -----------
    A : ndarray
        Input matrix
    
    Returns:
    --------
    U : ndarray
        Left singular vectors
    S : ndarray
        Singular values
    Vh : ndarray
        Transposed right singular vectors
    
    Examples:
    ---------
    >>> A = rand(3, 4)
    >>> U, S, Vh = svd(A)
    """
    return np.linalg.svd(A)


def norm(A: np.ndarray, ord: Union[None, int, float, str] = None) -> float:
    """
    Calculate vector or matrix norm
    
    Parameters:
    -----------
    A : ndarray
        Input array
    ord : {None, int, float, str}, optional
        Norm type
    
    Returns:
    --------
    float
        Norm value
    
    Examples:
    ---------
    >>> v = rand(5, 1)
    >>> n = norm(v)
    >>> n2 = norm(v, 2)
    """
    return np.linalg.norm(A, ord)


def dot(a: np.ndarray, b: np.ndarray) -> Union[float, np.ndarray]:
    """
    Calculate dot product
    
    Parameters:
    -----------
    a : ndarray
        First array
    b : ndarray
        Second array
    
    Returns:
    --------
    float or ndarray
        Dot product result
    
    Examples:
    ---------
    >>> a = rand(3, 1)
    >>> b = rand(3, 1)
    >>> c = dot(a, b)
    """
    return np.dot(a, b)


def cross(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Calculate cross product
    
    Parameters:
    -----------
    a : ndarray
        First vector
    b : ndarray
        Second vector
    
    Returns:
    --------
    ndarray
        Cross product result
    
    Examples:
    ---------
    >>> a = rand(3)
    >>> b = rand(3)
    >>> c = cross(a, b)
    """
    return np.cross(a, b)


def sum(A: np.ndarray, axis: Union[int, None] = None) -> Union[float, np.ndarray]:
    """
    Calculate sum
    
    Parameters:
    -----------
    A : ndarray
        Input array
    axis : int, optional
        Axis along which to compute the sum (None: 전체, 0: 열 방향, 1: 행 방향)
    
    Returns:
    --------
    float or ndarray
        Sum
    
    Examples:
    ---------
    >>> A = rand(3, 4)
    >>> s = sum(A)  # Total sum
    >>> s_col = sum(A, 0)  # Sum of each column
    >>> s_row = sum(A, 1)  # Sum of each row
    """
    return np.sum(A, axis=axis)


def mean(A: np.ndarray, axis: Union[int, None] = None) -> Union[float, np.ndarray]:
    """
    Calculate mean
    
    Parameters:
    -----------
    A : ndarray
        Input array
    axis : int, optional
        Axis along which to compute the mean
    
    Returns:
    --------
    float or ndarray
        Mean
    
    Examples:
    ---------
    >>> A = rand(3, 4)
    >>> m = mean(A)
    """
    return np.mean(A, axis=axis)


def std(A: np.ndarray, axis: Union[int, None] = None) -> Union[float, np.ndarray]:
    """
    Calculate standard deviation
    
    Parameters:
    -----------
    A : ndarray
        Input array
    axis : int, optional
        Axis along which to compute std
    
    Returns:
    --------
    float or ndarray
        Standard deviation
    
    Examples:
    ---------
    >>> A = rand(3, 4)
    >>> s = std(A)
    """
    return np.std(A, axis=axis)


def max(A: np.ndarray, axis: Union[int, None] = None) -> Union[float, np.ndarray]:
    """
    Calculate maximum value
    
    Parameters:
    -----------
    A : ndarray
        Input array
    axis : int, optional
        Axis along which to find maximum
    
    Returns:
    --------
    float or ndarray
        Maximum value
    
    Examples:
    ---------
    >>> A = rand(3, 4)
    >>> m = max(A)
    """
    return np.max(A, axis=axis)


def min(A: np.ndarray, axis: Union[int, None] = None) -> Union[float, np.ndarray]:
    """
    Calculate minimum value
    
    Parameters:
    -----------
    A : ndarray
        Input array
    axis : int, optional
        Axis along which to find minimum
    
    Returns:
    --------
    float or ndarray
        Minimum value
    
    Examples:
    ---------
    >>> A = rand(3, 4)
    >>> m = min(A)
    """
    return np.min(A, axis=axis)
