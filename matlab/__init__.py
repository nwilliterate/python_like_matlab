"""
Python Like MATLAB
A Python library for MATLAB addicts
"""

from .core import *
from .plotting import *
from .matrix import *
from .workspace import *

__version__ = "0.1.0"
__all__ = ['zeros', 'ones', 'linspace', 'meshgrid', 'rand', 'randn', 'eye', 'diag',
           'sin', 'cos', 'tan', 'exp', 'log', 'log10', 'sqrt', 'abs', 'floor', 'ceil', 'round',
           'figure', 'plot', 'subplot', 'xlabel', 'ylabel', 'title', 'legend', 'grid', 'show',
           'xlim', 'ylim', 'clf', 'close', 'savefig',
           'size', 'length', 'reshape', 'transpose', 'inv', 'det', 'eig', 'svd', 'norm',
           'dot', 'cross', 'sum', 'mean', 'std', 'max', 'min',
           'who', 'whos', 'clear', 'clc']
