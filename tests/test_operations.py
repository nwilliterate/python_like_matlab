#!/usr/bin/env python
"""
Test the MATLAB-style operations
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from matlab import *
import numpy as np
import re

def preprocess_matlab_syntax(command):
    """
    Preprocess MATLAB-style syntax to Python syntax
    
    - Convert ' (transpose) to .T
    - Convert [1,2,3] to np.array([1,2,3])
    """
    # Handle transpose operator: convert a' to a.T
    # Use regex to find variable names followed by '
    command = re.sub(r'(\w+)\'', r'\1.T', command)
    
    # Convert matrix/vector literals to numpy arrays
    # Match [...] patterns and wrap them with np.array()
    def replace_brackets(match):
        content = match.group(1)
        return f'np.array([{content}])'
    
    # Only convert brackets that look like matrix literals (not function calls)
    # Match [...] that are not preceded by a letter/underscore (to avoid matching func[...])
    command = re.sub(r'(?<![a-zA-Z_])\[([^\[\]]+)\]', replace_brackets, command)
    
    return command

# Test cases
print("Testing MATLAB-style operations:")
print("=" * 60)

local_vars = {}

# Test 1: Create arrays
print("\nTest 1: Creating arrays")
command = "a = [1, 2, 3]"
processed = preprocess_matlab_syntax(command)
print(f"Command: {command}")
print(f"Processed: {processed}")
exec(processed, globals(), local_vars)
for key, value in local_vars.items():
    if isinstance(value, list):
        local_vars[key] = np.array(value)
print(f"a = {local_vars['a']}")
print(f"Type: {type(local_vars['a'])}")

command = "b = [4, 5, 6]"
processed = preprocess_matlab_syntax(command)
print(f"\nCommand: {command}")
print(f"Processed: {processed}")
exec(processed, globals(), local_vars)
for key, value in local_vars.items():
    if isinstance(value, list):
        local_vars[key] = np.array(value)
print(f"b = {local_vars['b']}")
print(f"Type: {type(local_vars['b'])}")

# Test 2: Element-wise multiplication
print("\n" + "=" * 60)
print("Test 2: Element-wise multiplication")
command = "a * b"
processed = preprocess_matlab_syntax(command)
print(f"Command: {command}")
print(f"Processed: {processed}")
namespace = globals().copy()
namespace.update(local_vars)
result = eval(processed, namespace, local_vars)
print(f"Result: {result}")

# Test 3: Transpose
print("\n" + "=" * 60)
print("Test 3: Transpose")
command = "a'"
processed = preprocess_matlab_syntax(command)
print(f"Command: {command}")
print(f"Processed: {processed}")
namespace = globals().copy()
namespace.update(local_vars)
result = eval(processed, namespace, local_vars)
print(f"Result: {result}")

# Test 4: Matrix multiplication with transpose
print("\n" + "=" * 60)
print("Test 4: Matrix multiplication with transpose")
command = "A = [[1, 2], [3, 4]]"
processed = preprocess_matlab_syntax(command)
print(f"Command: {command}")
print(f"Processed: {processed}")
exec(processed, globals(), local_vars)
for key, value in local_vars.items():
    if isinstance(value, list):
        local_vars[key] = np.array(value)
print(f"A = \n{local_vars['A']}")

command = "A'"
processed = preprocess_matlab_syntax(command)
print(f"\nCommand: {command}")
print(f"Processed: {processed}")
namespace = globals().copy()
namespace.update(local_vars)
result = eval(processed, namespace, local_vars)
print(f"Result: \n{result}")

# Test 5: Matrix multiplication
print("\n" + "=" * 60)
print("Test 5: Matrix multiplication (use @ operator)")
print("For matrix multiplication, use @ operator like: A @ B")
command = "A @ A'"
processed = preprocess_matlab_syntax(command)
print(f"Command: {command}")
print(f"Processed: {processed}")
namespace = globals().copy()
namespace.update(local_vars)
result = eval(processed, namespace, local_vars)
print(f"Result: \n{result}")

print("\n" + "=" * 60)
print("All tests completed!")
