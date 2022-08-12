import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector


def line_select_callback(eclick,
                         erelease):
    '''
    eclick and erelease are the press and release events
    '''
    global x1, y1, x2, y2
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print('(%3.2f, %3.2f) --> (%3.2f, %3.2f)' % (x1, y1, x2, y2))
    print('The button you used were: %s %s' % (eclick.button, erelease.button))
    return x1, y1, x2, y2


def toggle_selector(event):
    '''
    Toggle selector determines if a key has been pressed
    '''
    print('Key Pressed')
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print('RectangleSelector Deactivated')
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print('RectangleSelector Activated')
        toggle_selector.RS.set_active(True)


def graph_of_interest(x, y,
                      file_name):
    '''
    Allows user to select an area of a graph of interest. Plots an x-y graph
    and uses matplotlib rectangle selector to select region of interest. The
    x,y coordinates for the region are returned.
    Args:
        x: <array> x-axis data
        y: <array> y-axis data
        file_name: <string> file identifier for the data label
    Returns:
        x1, y1: <float> x and y coordinates for the start position of the box
        x2, y2: <float> x and y coordinates for the end position of the box
    '''
    fig, ax = plt.subplots()
    ax.plot(
        x,
        y,
        'red',
        lw=2,
        label=file_name)
    ax.legend(
        frameon=True,
        loc=0,
        prop={'size': 14})
    ax.grid(True)
    ax.tick_params(
        axis='both',
        colors='black',
        labelsize=12)
    ax.set_xlabel(
        'x',
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_ylabel(
        'y',
        fontsize=14,
        fontweight='bold',
        color='black')
    print('\n   click  -->  release')
    toggle_selector.RS = RectangleSelector(
        ax,
        line_select_callback,
        drawtype='box',
        useblit=True,
        button=[1, 3],
        minspanx=5,
        minspany=5,
        spancoords='pixels',
        interactive=True)
    plt.connect(
        'key_press_event',
        toggle_selector)
    plt.show()
    return x1, y1, x2, y2


def region_of_interest(x, y,
                       file_name):
    '''
    Trim arrays to match region of interest. Select area of interest on graph,
    using matplotlib rectangle selector. Returns trimmed arrays to match region
    of interest.
    Args:
        x: <array> x-axis data
        y: <array> y-axis data
        file_name: <string> file identifier for the data label
    Returns:
        x_interest: <array> trimmed x-array
        y_interest: <array> trimmed y-array
        x1: <float> initial region of interest x-coordinate
        x2: <float> final region of interest x-coordinate
    '''
    x1, _, x2, _ = graph_of_interest(
        x=x,
        y=y,
        file_name=file_name)
    min_index = np.argmin(np.abs(x - x1))
    max_index = np.argmin(np.abs(x - x2))
    x_interest = x[min_index: max_index]
    y_interest = y[min_index: max_index]
    return x_interest, y_interest, x1, x2
