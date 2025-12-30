# Python Like MATLAB

A Python library for MATLAB users - Write Python code in MATLAB style!

> **Note:** MATLAB® is a registered trademark of The MathWorks, Inc. This project is not affiliated with, endorsed by, or sponsored by The MathWorks, Inc.

## Introduction

This library provides a MATLAB-style interface for Python, making it easier for MATLAB users to transition to Python. Built on NumPy and Matplotlib, it offers familiar function names and syntax while leveraging Python's ecosystem.

## Installation

### Automated Installation (Recommended)

After downloading the project, run the script for your operating system:

**Windows:**
```bash
setup_env.bat
```

**Linux/Mac:**
```bash
chmod +x setup_env.sh
./setup_env.sh
```

The script will automatically:
- Create virtual environment
- Install required packages
- Configure environment

Activate virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Manual Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

Required packages:
- numpy >= 1.21.0
- matplotlib >= 3.4.0
- scipy >= 1.7.0

## Quick Start

### Method 1: Use in Python Scripts

```python
from matlab import *

# Create arrays and compute in MATLAB style
x = linspace(0, 2*pi, 100)
y = sin(x)

# MATLAB-style plotting
figure()
plot(x, y, 'b-', linewidth=2)
xlabel('x')
ylabel('sin(x)')
title('MATLAB Style Plot')
grid('on')
show()
```

### Method 2: MATLAB-Style Interpreter (Recommended)

IPython-based interactive interpreter:

```bash
python matlab_interpreter.py
```

Use like MATLAB in the interpreter:
```matlab
>> x = linspace(0, 10, 100)
>> y = sin(x)
>> figure()
>> plot(x, y, 'r-')
>> xlabel('x')
>> ylabel('y')
>> grid('on')
>> show()
>> who
>> whos
```

Simple REPL also available:
```bash
python matlab_repl.py
```

### Method 3: Jupyter Notebook

```bash
cd examples
jupyter notebook
```

Available notebooks:
- `quick_start.ipynb` - 5-minute quick start guide
- `matlab_style_tutorial.ipynb` - Complete feature tutorial

### Method 4: IPython Auto-Configuration

To automatically load the MATLAB environment when starting IPython:

```bash
# Check IPython profile directory
ipython profile locate

# Copy startup_matlab.py (refer to the path from the command above)
cp startup_matlab.py ~/.ipython/profile_default/startup/

# MATLAB functions are automatically loaded when starting IPython
ipython
```

## Key Features

### Array Creation and Manipulation
- `zeros(m, n)` - Create array filled with zeros
- `ones(m, n)` - Create array filled with ones
- `eye(n)` - Identity matrix
- `linspace(start, stop, num)` - Evenly spaced array
- `meshgrid(x, y)` - Create coordinate grids
- `rand(m, n)` - Uniform random array
- `randn(m, n)` - Normal distribution random array
- `diag(v)` - Create/extract diagonal matrix
- `reshape(A, m, n)` - Reshape array
- `transpose(A)` - Transpose

### Mathematical Functions
- `sin, cos, tan` - Trigonometric functions
- `exp, log, log10` - Exponential/logarithmic functions
- `sqrt, abs` - Square root, absolute value
- `floor, ceil, round` - Rounding functions

### Linear Algebra
- `inv(A)` - Matrix inverse
- `det(A)` - Determinant
- `eig(A)` - Eigenvalues/eigenvectors
- `svd(A)` - Singular value decomposition
- `norm(A)` - Norm
- `dot(a, b)` - Dot product
- `cross(a, b)` - Cross product

### Statistical Functions
- `mean(A)` - Mean
- `std(A)` - Standard deviation
- `sum(A)` - Sum
- `max(A), min(A)` - Maximum, minimum

### Plotting
- `figure()` - New figure window
- `plot(x, y, style)` - 2D line plot
- `subplot(m, n, p)` - Create subplot
- `xlabel(), ylabel(), title()` - Labels and title
- `grid(option)` - Grid display
- `legend(labels)` - Legend
- `xlim(limits), ylim(limits)` - Axis limits
- `clf()` - Clear current figure
- `close()` - Close figure
- `savefig(filename)` - Save figure
- `show()` - Display plot

### Workspace Management
- `who()` - List variables
- `whos()` - Detailed variable information
- `clear(*names)` - Delete variables
- `clc()` - Clear console screen

## Examples

See the `examples/` directory for detailed examples:

- [basic_usage.py](examples/basic_usage.py) - Basic usage
- [linear_algebra.py](examples/linear_algebra.py) - Linear algebra examples
- [signal_processing.py](examples/signal_processing.py) - Signal processing examples

## Project Structure

```
python_like_matlab/
├── matlab/              # Core library
│   ├── __init__.py
│   ├── core.py         # Basic array and math functions
│   ├── matrix.py       # Linear algebra functions
│   ├── plotting.py     # Plotting functions
│   └── workspace.py    # Workspace management
├── examples/           # Example scripts and notebooks
├── tests/             # Test code
├── matlab_interpreter.py  # IPython-based interpreter
├── matlab_repl.py        # Simple REPL
├── startup_matlab.py     # IPython startup script
└── README.md
```

## Testing

```bash
python tests/test_core.py
```

## License

MIT License

## Disclaimer

This project is an independent open-source implementation and is not affiliated with, endorsed by, or sponsored by The MathWorks, Inc. MATLAB® is a registered trademark of The MathWorks, Inc.

## Contributing

Issues and pull requests are welcome!
