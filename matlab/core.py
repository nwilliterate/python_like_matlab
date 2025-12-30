"""
MATLAB-style core functions
"""

import numpy as np
from typing import Union, Tuple, Optional


def zeros(m: int, n: Optional[int] = None) -> np.ndarray:
    """
    Create an array filled with zeros
    
    Parameters:
    -----------
    m : int
        Number of rows
    n : int, optional
        Number of columns (if omitted, creates m x m square matrix)
    
    Returns:
    --------
    ndarray
        Array filled with zeros
    
    Examples:
    ---------
    >>> A = zeros(3, 4)
    >>> B = zeros(5)
    """
    if n is None:
        return np.zeros((m, m))
    return np.zeros((m, n))


def ones(m: int, n: Optional[int] = None) -> np.ndarray:
    """
    Create an array filled with ones
    
    Parameters:
    -----------
    m : int
        Number of rows
    n : int, optional
        Number of columns (if omitted, creates m x m square matrix)
    
    Returns:
    --------
    ndarray
        Array filled with ones
    
    Examples:
    ---------
    >>> A = ones(3, 4)
    >>> B = ones(5)
    """
    if n is None:
        return np.ones((m, m))
    return np.ones((m, n))


def linspace(start: float, stop: float, num: int = 50) -> np.ndarray:
    """
    Create an array with evenly spaced values
    
    Parameters:
    -----------
    start : float
        Starting value
    stop : float
        Ending value
    num : int, optional
        Number of values to generate (default: 50)
    
    Returns:
    --------
    ndarray
        Array with evenly spaced values
    
    Examples:
    ---------
    >>> x = linspace(0, 10, 100)
    """
    return np.linspace(start, stop, num)


def meshgrid(x: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create coordinate matrices from coordinate vectors
    
    Parameters:
    -----------
    x : ndarray
        x-coordinate vector
    y : ndarray
        y-coordinate vector
    
    Returns:
    --------
    X, Y : ndarray
        Coordinate matrices
    
    Examples:
    ---------
    >>> x = linspace(0, 1, 10)
    >>> y = linspace(0, 1, 10)
    >>> X, Y = meshgrid(x, y)
    """
    return np.meshgrid(x, y)


def rand(m: int, n: Optional[int] = None) -> np.ndarray:
    """
    Create a random array with uniform distribution [0, 1)
    
    Parameters:
    -----------
    m : int
        Number of rows
    n : int, optional
        Number of columns (if omitted, creates m x m square matrix)
    
    Returns:
    --------
    ndarray
        Random array
    
    Examples:
    ---------
    >>> A = rand(3, 4)
    >>> B = rand(5)
    """
    if n is None:
        return np.random.rand(m, m)
    return np.random.rand(m, n)


def randn(m: int, n: Optional[int] = None) -> np.ndarray:
    """
    Create a random array with standard normal distribution
    
    Parameters:
    -----------
    m : int
        Number of rows
    n : int, optional
        Number of columns (if omitted, creates m x m square matrix)
    
    Returns:
    --------
    ndarray
        Random array
    
    Examples:
    ---------
    >>> A = randn(3, 4)
    >>> B = randn(5)
    """
    if n is None:
        return np.random.randn(m, m)
    return np.random.randn(m, n)


def eye(n: int, m: Optional[int] = None) -> np.ndarray:
    """
    Create an identity matrix
    
    Parameters:
    -----------
    n : int
        Number of rows
    m : int, optional
        Number of columns (if omitted, creates n x n square matrix)
    
    Returns:
    --------
    ndarray
        Identity matrix
    
    Examples:
    ---------
    >>> I = eye(3)
    >>> A = eye(3, 4)
    """
    if m is None:
        return np.eye(n)
    return np.eye(n, m)


def diag(v: Union[np.ndarray, list], k: int = 0) -> np.ndarray:
    """
    Create a diagonal matrix or extract diagonal elements
    
    Parameters:
    -----------
    v : ndarray or list
        Vector or matrix
    k : int, optional
        Diagonal offset (default: 0)
    
    Returns:
    --------
    ndarray
        Diagonal matrix or diagonal elements
    
    Examples:
    ---------
    >>> D = diag([1, 2, 3])
    >>> v = diag(A)
    """
    return np.diag(v, k)


# MATLAB-style mathematical functions
sin = np.sin
cos = np.cos
tan = np.tan
exp = np.exp
log = np.log
log10 = np.log10
sqrt = np.sqrt
abs = np.abs
floor = np.floor
ceil = np.ceil
round = np.round
