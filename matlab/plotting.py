"""
MATLAB-style plotting functions
"""

import matplotlib.pyplot as plt
from matplotlib.legend import Legend
from typing import Optional, Union, List


# Global figure counter
_figure_counter = 0


def figure(num: Optional[int] = None, figsize: Optional[tuple] = None) -> plt.Figure:
    """
    Create a new figure window
    
    Parameters:
    -----------
    num : int, optional
        figure number
    figsize : tuple, optional
        figure size (width, height)
    
    Returns:
    --------
    Figure
        matplotlib Figure object
    
    Examples:
    ---------
    >>> figure()
    >>> figure(1)
    >>> figure(figsize=(10, 6))
    """
    global _figure_counter
    if num is None:
        _figure_counter += 1
        num = _figure_counter
    
    return plt.figure(num, figsize=figsize)


def plot(*args, **kwargs) -> List[plt.Line2D]:
    """
    Plot line graph
    
    Parameters:
    -----------
    *args : 
        x, y Data and style string
        plot(y)
        plot(x, y)
        plot(x, y, 'style')
    **kwargs : 
        Additional plot options (linewidth, color, label, etc.)
    
    Returns:
    --------
    list of Line2D
        Created line objects
    
    Examples:
    ---------
    >>> plot(y)
    >>> plot(x, y)
    >>> plot(x, y, 'r-')
    >>> plot(x, y, 'b--', linewidth=2)
    """
    return plt.plot(*args, **kwargs)


def subplot(m: int, n: int, p: int) -> plt.Axes:
    """
    Create subplot
    
    Parameters:
    -----------
    m : int
        Number of rows
    n : int
        Number of columns
    p : int
        Plot position (starting from 1)
    
    Returns:
    --------
    Axes
        matplotlib Axes object
    
    Examples:
    ---------
    >>> subplot(2, 2, 1)
    >>> plot(x, y1)
    >>> subplot(2, 2, 2)
    >>> plot(x, y2)
    """
    return plt.subplot(m, n, p)


def xlabel(label: str, **kwargs) -> None:
    """
    Set x-axis label
    
    Parameters:
    -----------
    label : str
        x-axis label
    **kwargs : 
        Additional options (fontsize, color, etc.)
    
    Examples:
    ---------
    >>> xlabel('Time (s)')
    >>> xlabel('Time (s)', fontsize=14)
    """
    plt.xlabel(label, **kwargs)


def ylabel(label: str, **kwargs) -> None:
    """
    Set y-axis label
    
    Parameters:
    -----------
    label : str
        y-axis label
    **kwargs : 
        Additional options (fontsize, color, etc.)
    
    Examples:
    ---------
    >>> ylabel('Amplitude')
    >>> ylabel('Amplitude', fontsize=14)
    """
    plt.ylabel(label, **kwargs)


def title(label: str, **kwargs) -> None:
    """
    Set title
    
    Parameters:
    -----------
    label : str
        Title text
    **kwargs : 
        Additional options (fontsize, color, etc.)
    
    Examples:
    ---------
    >>> title('My Plot')
    >>> title('My Plot', fontsize=16)
    """
    plt.title(label, **kwargs)


def legend(*args, **kwargs) -> Legend:
    """
    Add legend
    
    Parameters:
    -----------
    *args : 
        List of legend labels
    **kwargs : 
        Additional options (loc, fontsize, etc.)
    
    Returns:
    --------
    Legend
        matplotlib Legend object
    
    Examples:
    ---------
    >>> plot(x, y1, label='Data 1')
    >>> plot(x, y2, label='Data 2')
    >>> legend()
    >>> legend(['Data 1', 'Data 2'])
    """
    return plt.legend(*args, **kwargs)


def grid(state: Union[bool, str] = True) -> None:
    """
    Set grid display
    
    Parameters:
    -----------
    state : bool or str
        True, 'on' - Show grid
        False, 'off' - Hide grid
    
    Examples:
    ---------
    >>> grid()
    >>> grid('on')
    >>> grid('off')
    """
    if isinstance(state, str):
        state = state.lower() == 'on'
    plt.grid(state)


def xlim(left: Optional[float] = None, right: Optional[float] = None) -> tuple:
    """
    Set x-axis limits
    
    Parameters:
    -----------
    left : float, optional
        x-axis minimum
    right : float, optional
        x-axis maximum
    
    Returns:
    --------
    tuple
        Current x-axis limits (left, right)
    
    Examples:
    ---------
    >>> xlim(0, 10)
    >>> xlim(left=0)
    """
    return plt.xlim(left, right)


def ylim(bottom: Optional[float] = None, top: Optional[float] = None) -> tuple:
    """
    Set y-axis limits
    
    Parameters:
    -----------
    bottom : float, optional
        y-axis minimum
    top : float, optional
        y-axis maximum
    
    Returns:
    --------
    tuple
        Current y-axis limits (bottom, top)
    
    Examples:
    ---------
    >>> ylim(0, 1)
    >>> ylim(bottom=0)
    """
    return plt.ylim(bottom, top)


def show() -> None:
    """
    Display graph
    
    Examples:
    ---------
    >>> plot(x, y)
    >>> show()
    """
    plt.show()


def clf() -> None:
    """
    Clear current figure
    
    Examples:
    ---------
    >>> clf()
    """
    plt.clf()


def close(num: Optional[Union[int, str]] = None) -> None:
    """
    Close figure
    
    Parameters:
    -----------
    num : int or str, optional
        Figure number to close or 'all'
    
    Examples:
    ---------
    >>> close()
    >>> close(1)
    >>> close('all')
    """
    if num is None:
        plt.close()
    else:
        plt.close(num)


def savefig(filename: str, **kwargs) -> None:
    """
    Save figure to file
    
    Parameters:
    -----------
    filename : str
        Filename to save
    **kwargs : 
        Additional options (dpi, format 등)
    
    Examples:
    ---------
    >>> savefig('plot.png')
    >>> savefig('plot.pdf', dpi=300)
    """
    plt.savefig(filename, **kwargs)
