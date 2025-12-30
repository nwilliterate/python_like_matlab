"""
MATLAB-style workspace management functions
"""

import sys
import numpy as np
from typing import Optional


def who(pattern: Optional[str] = None) -> None:
    """
    Print list of variables in current workspace
    
    Parameters:
    -----------
    pattern : str, optional
        Pattern to filter
    
    Examples:
    ---------
    >>> A = zeros(3, 4)
    >>> B = ones(2, 2)
    >>> who()
    """
    frame = sys._getframe(1)
    variables = frame.f_locals
    
    var_names = []
    for name, value in variables.items():
        if not name.startswith('_'):
            if pattern is None or pattern in name:
                var_names.append(name)
    
    if var_names:
        print("Variables in workspace:")
        for name in sorted(var_names):
            print(f"  {name}")
    else:
        print("No variables.")


def whos(pattern: Optional[str] = None) -> None:
    """
    Print detailed information about variables
    
    Parameters:
    -----------
    pattern : str, optional
        Pattern to filter
    
    Examples:
    ---------
    >>> A = zeros(3, 4)
    >>> B = ones(2, 2)
    >>> whos()
    """
    frame = sys._getframe(1)
    variables = frame.f_locals
    
    print(f"{'Name':<15} {'Size':<20} {'Type':<15}")
    print("-" * 50)
    
    for name, value in sorted(variables.items()):
        if not name.startswith('_'):
            if pattern is None or pattern in name:
                if isinstance(value, np.ndarray):
                    size_str = f"{value.shape}"
                    type_str = f"ndarray ({value.dtype})"
                elif isinstance(value, (list, tuple)):
                    size_str = f"({len(value)},)"
                    type_str = type(value).__name__
                else:
                    size_str = "-"
                    type_str = type(value).__name__
                
                print(f"{name:<15} {size_str:<20} {type_str:<15}")


def clear(*var_names) -> None:
    """
    Delete variables from workspace
    
    Parameters:
    -----------
    *var_names : str
        Variable names to delete (if no arguments, delete all variables)
    
    Examples:
    ---------
    >>> clear('A')
    >>> clear('A', 'B', 'C')
    >>> clear()  # Delete all variables
    """
    frame = sys._getframe(1)
    variables = frame.f_locals
    
    if not var_names:
        # Delete all user variables
        to_delete = [name for name in variables.keys() if not name.startswith('_')]
        for name in to_delete:
            del variables[name]
        print(f"{len(to_delete)} variables deleted.")
    else:
        # Delete specific variables
        deleted = 0
        for name in var_names:
            if name in variables:
                del variables[name]
                deleted += 1
            else:
                print(f"Warning: variable '{name}' not found.")
        
        if deleted > 0:
            print(f"{deleted} variables deleted.")


def clc() -> None:
    """
    Clear console screen
    
    Examples:
    ---------
    >>> clc()
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
