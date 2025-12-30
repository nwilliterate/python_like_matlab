# IPython startup script
# Automatically configures IPython in MATLAB style.
#
# Usage:
# 1. Check IPython profile directory: ipython profile locate
# 2. Copy this file: cp startup_matlab.py ~/.ipython/profile_default/startup/
# 3. Run IPython: ipython

import sys
import os

# Add matlab package path (modify if needed)
# sys.path.insert(0, '/path/to/python_like_matlab')

try:
    from matlab import *
    
    print("=" * 70)
    print("MATLAB-style Python environment loaded!")
    print("=" * 70)
    print()
    print("Available functions:")
    print("  Arrays: zeros, ones, eye, rand, randn, linspace, meshgrid")
    print("  Math: sin, cos, tan, exp, log, sqrt, abs")
    print("  Plotting: figure, plot, subplot, xlabel, ylabel, title, legend, grid, show")
    print("  Matrix: inv, det, eig, svd, transpose, dot, cross")
    print("  Statistics: mean, std, sum, max, min")
    print("  Workspace: who(), whos(), clear()")
    print()
    print("Example:")
    print("  x = linspace(0, 10, 100)")
    print("  y = sin(x)")
    print("  plot(x, y)")
    print("  show()")
    print("=" * 70)
    print()
    
except ImportError as e:
    print(f"Warning: Cannot load matlab package: {e}")
    print("Please check your sys.path.")
