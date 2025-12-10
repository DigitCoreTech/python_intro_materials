import numpy as np

# plot height vs weight
import matplotlib.pyplot as plt

def plot_height_vs_weight(df, height_col, weight_col):
    """Plot height vs weight with linear fit.
    
    Args:
        df: DataFrame containing the data
        height_col: Name of the height column
        weight_col: Name of the weight column
    
    Returns:
        matplotlib.figure.Figure: The generated figure
    """
    fig, ax = plt.subplots()
    
    ax.scatter(df[height_col], df[weight_col])
    
    # Add linear approximation
    z = np.polyfit(df[height_col], df[weight_col], 1)
    p = np.poly1d(z)
    ax.plot(df[height_col], p(df[height_col]), "r-", label='Linear fit')
    
    ax.set_xlabel('Height (Inches)')
    ax.set_ylabel('Weight (Pounds)')
    ax.set_title('Height vs Weight. PLOT 1')
    ax.legend()
    
    return fig


def add(a: int, b: int, c: int = 0) -> int:
    return a + b + c


def concatenate_strings(s1: str, s2: str) -> str:
    return add(s1, s2)
