#!/usr/bin/env python
"""
Simple MATLAB-style REPL
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from matlab import *
import numpy as np

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
                # Include both matlab functions and local variables in global namespace
                namespace = globals().copy()
                namespace.update(local_vars)
                
                # Execute
                result = eval(command, namespace, local_vars)
                
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
                    namespace = globals().copy()
                    namespace.update(local_vars)
                    exec(command, namespace, local_vars)
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
