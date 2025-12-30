#!/usr/bin/env python
"""
Simple MATLAB-style REPL
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

def main():
    print("=" * 60)
    print("MATLAB Style Python REPL")
    print("=" * 60)
    print("Enter commands (exit: exit, help: help)")
    print()
    
    # Local variable storage
    local_vars = {}
    
    while True:
        try:
            # Display prompt
            command = input(">> ")
            
            # Empty input
            if not command.strip():
                continue
            
            # Exit command
            if command.strip().lower() in ['exit', 'quit', 'exit()', 'quit()']:
                print("Exiting.")
                break
            
            # help
            if command.strip().lower() == 'help':
                print("\nAvailable functions:")
                print("  zeros, ones, eye, rand, randn, linspace, meshgrid")
                print("  sin, cos, tan, exp, log, sqrt, abs")
                print("  figure, plot, subplot, xlabel, ylabel, title, legend, grid, show")
                print("  inv, det, eig, svd, transpose, dot, cross")
                print("  mean, std, sum, max, min")
                print("  who(), whos(), clear()\n")
                continue
            
            # Special handling for who command
            if command.strip() in ['who', 'who()']:
                if local_vars:
                    print("Variables in workspace:")
                    for name in sorted(local_vars.keys()):
                        print(f"  {name}")
                else:
                    print("No variables.")
                continue
            
            # Special handling for whos command
            if command.strip() in ['whos', 'whos()']:
                if local_vars:
                    print(f"{'Name':<15} {'Size':<20} {'Type':<15}")
                    print("-" * 50)
                    for name, value in sorted(local_vars.items()):
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
                else:
                    print("No variables.")
                continue
            
            # Execute command
            try:
                # Preprocess MATLAB-style syntax
                processed_command = preprocess_matlab_syntax(command)
                
                # Include both matlab functions and local variables in global namespace
                namespace = globals().copy()
                namespace.update(local_vars)
                
                # Execute
                result = eval(processed_command, namespace, local_vars)
                
                # Convert lists to numpy arrays if needed
                if isinstance(result, list):
                    result = np.array(result)
                
                # Display result
                if result is not None:
                    print(f"ans = ")
                    if isinstance(result, np.ndarray):
                        print(result)
                    else:
                        print(result)
                    # Store in ans variable
                    local_vars['ans'] = result
                    
            except SyntaxError:
                # If eval fails, try exec (for assignments, etc.)
                try:
                    processed_command = preprocess_matlab_syntax(command)
                    namespace = globals().copy()
                    namespace.update(local_vars)
                    exec(processed_command, namespace, local_vars)
                    
                    # Convert any newly created list variables to numpy arrays
                    for key, value in local_vars.items():
                        if isinstance(value, list):
                            local_vars[key] = np.array(value)
                except Exception as e:
                    print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")
                
        except EOFError:
            print("\nExiting.")
            break
        except KeyboardInterrupt:
            print("\n^C")
            continue

if __name__ == '__main__':
    main()
