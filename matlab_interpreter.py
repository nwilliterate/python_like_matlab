#!/usr/bin/env python
"""
MATLAB-style interpreter
Use Python interactively like MATLAB.
"""

import sys
import os

# Add package path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import MATLAB-style functions into global namespace
from matlab import *

def print_banner():
    """Print startup banner"""
    print("=" * 70)
    print("Python Like MATLAB - Interactive Interpreter")
    print("=" * 70)
    print("Use Python in MATLAB style!")
    print()
    print("Available functions:")
    print("  Arrays: zeros, ones, eye, rand, randn, linspace, meshgrid")
    print("  Math: sin, cos, tan, exp, log, sqrt, abs")
    print("  Plotting: figure, plot, subplot, xlabel, ylabel, title, legend, grid, show")
    print("  Matrix: inv, det, eig, svd, transpose, dot, cross")
    print("  Statistics: mean, std, sum, max, min")
    print("  Workspace: who(), whos(), clear()")
    print()
    print("To exit, enter 'exit' or press Ctrl+D.")
    print("=" * 70)
    print()

def main():
    """Main interpreter loop"""
    print_banner()
    
    # Prepare global namespace
    global_namespace = globals().copy()
    local_namespace = {}
    
    try:
        # Use IPython if installed
        try:
            from IPython import embed
            from IPython.terminal.prompts import Prompts, Token
            
            # MATLAB-style prompt
            class MatlabPrompt(Prompts):
                def in_prompt_tokens(self):
                    return [
                        (Token.Prompt, '>> '),
                    ]
                
                def out_prompt_tokens(self):
                    return [
                        (Token.OutPrompt, 'ans = '),
                    ]
            
            # IPython configuration
            from traitlets.config import Config
            c = Config()
            c.TerminalInteractiveShell.prompts_class = MatlabPrompt
            c.TerminalInteractiveShell.confirm_exit = False
            
            # Start IPython session
            embed(config=c, user_ns=global_namespace)
            
        except ImportError:
            # Use basic Python interpreter if IPython is not available
            import code
            
            console = code.InteractiveConsole(global_namespace)
            console.interact()
            
    except (EOFError, KeyboardInterrupt):
        print("\n\nExiting. Goodbye!")

if __name__ == '__main__':
    main()
