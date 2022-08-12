import numpy as np
import matplotlib.pyplot as plt


def xy_plot(x, y, label, color,
            xlabel, ylabel, title, out_path,
            line=False, show=False):
    '''
    Standard, one-axis, x-y plot.
    Args:
        x: <array> x-data array
        y: <array> y-data array
        color: <string> matplotlib color identifier
        xlabel: <string> x-axis label
        ylabel: <string> y-axis label
        label: <string> data label
        title: <string> plot title
        out_path: <string> save path
        line: <bool> if true, plots line, else plots markers
        show: <bool> if true, plot shows, always saves
    Returns:
        None
    '''
    fig, ax = plt.subplots(
        1,
        figsize=[10, 7])
    if line:
        ax.plot(
            x, y,
            f'{color}',
            lw=2,
            label=label)
    else:
        ax.plot(
            x, y,
            f'{color}x',
            markersize=4,
            label=label)
    ax.grid(True)
    ax.legend(
        frameon=True,
        loc=0,
        prop={'size': 14})
    ax.set_xlabel(
        xlabel,
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_ylabel(
        ylabel,
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_title(
        title,
        fontsize=18,
        fontweight='bold',
        color='black')
    ax.tick_params(
        axis='both',
        colors='black',
        labelsize=14)
    if show:
        plt.show()
    plt.savefig(out_path)
    fig.clf()
    plt.cla()
    plt.close(fig)


def xy_roi_plot(x, y, label, color,
                x1, x2, vline_color, text_string,
                xlabel, ylabel, title, out_path,
                line=False, show=False):
    '''
    Plot region of interest for (x, y) data on graph. Display start and end of
    region of interest on x-axis.
    Args:
        x: <array> x-data array
        y: <array> y-data array
        color: <string> matplotlib color identifier
        x1: <float> initial x-coordinate for region of interest
        x2: <float> final x-coordinate for region of interest
        vline_color: <string> matplotlib color indentifier
        text_string: <string> text string for display box
        xlabel: <string> x-axis label
        ylabel: <string> y-axis label
        label: <string> data label
        title: <string> plot title
        out_path: <string> save path
        line: <bool> if true, plots line, else plots markers
        show: <bool> if true, plot shows, always saves
    Returns:
        None
    '''
    fig, ax = plt.subplots(
        1,
        figsize=[10, 7])
    if line:
        ax.plot(
            x, y,
            f'{color}',
            lw=2,
            label=label)
    else:
        ax.plot(
            x, y,
            f'{color}x',
            markersize=4,
            label=label)
    ax.grid(True)
    ax.legend(
        frameon=True,
        loc=0,
        prop={'size': 14})
    ax.axvline(
        x=x1,
        color=f'{vline_color}',
        linestyle='--')
    ax.axvline(
        x=x2,
        color=f'{vline_color}',
        linestyle='--')
    ax.set_xlabel(
        xlabel,
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_ylabel(
        ylabel,
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_title(
        title,
        fontsize=18,
        fontweight='bold',
        color='black')
    ax.tick_params(
        axis='both',
        colors='black',
        labelsize=14)
    props = dict(
        boxstyle='round',
        facecolor='wheat',
        alpha=0.5)
    ax.text(
        0.05,
        0.05,
        text_string,
        transform=ax.transAxes,
        fontsize=14,
        verticalalignment='top',
        bbox=props)
    plt.savefig(out_path)
    fig.clf()
    plt.cla()
    plt.close(fig)


def xy_tworoi_plot(x, y, label, color,
                   x1, x2, x3, x4, vline_color, text_string,
                   xlabel, ylabel, title, out_path,
                   line=False, show=False):
    '''
    Plot two regions of interest for (x, y) data on graph. Display start and
    end of regions of interest on x-axis.
    Args:
        x: <array> x-data array
        y: <array> y-data array
        color: <string> matplotlib color identifier
        x1: <float> initial x-coordinate for region of interest 1
        x2: <float> final x-coordinate for region of interest 1
        x3: <float> initial x-coordinate for region of interest 2
        x4: <float> final x-coordinate for region of interest 2
        vline_color: <string> matplotlib color indentifier
        text_string: <string> text string for display box
        xlabel: <string> x-axis label
        ylabel: <string> y-axis label
        label: <string> data label
        title: <string> plot title
        out_path: <string> save path
        line: <bool> if true, plots line, else plots markers
        show: <bool> if true, plot shows, always saves
    Returns:
        None
    '''
    fig, ax = plt.subplots(
                1,
                figsize=[10, 7])
    if line:
        ax.plot(
            x, y,
            f'{color}',
            lw=2,
            label=label)
    else:
        ax.plot(
            x, y,
            f'{color}x',
            markersize=4,
            label=label)
    ax.grid(True)
    ax.legend(
        frameon=True,
        loc=0,
        prop={'size': 14})
    ax.axvline(
        x=x1,
        color=f'{vline_color}',
        linestyle='--')
    ax.axvline(
        x=x2,
        color=f'{vline_color}',
        linestyle='--')
    ax.axvline(
        x=x3,
        color=f'{vline_color}',
        linestyle='--')
    ax.axvline(
        x=x4,
        color=f'{vline_color}',
        linestyle='--')
    ax.set_xlabel(
        xlabel,
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_ylabel(
        ylabel,
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_title(
        title,
        fontsize=18,
        fontweight='bold',
        color='black')
    ax.tick_params(
        axis='both',
        colors='black',
        labelsize=14)
    props = dict(
        boxstyle='round',
        facecolor='wheat',
        alpha=0.5)
    ax.text(
        0.05,
        0.05,
        text_string,
        transform=ax.transAxes,
        fontsize=14,
        verticalalignment='top',
        bbox=props)
    plt.savefig(out_path)
    fig.clf()
    plt.cla()
    plt.close(fig)


def xy_error_plot(x, x_error, y, y_error,
                  label, color,
                  xlabel, ylabel, title, out_path,
                  line=False, show=False):
    '''
    Standard, one-axis, x-y plot with error bars.
    Args:
        x: <array> x-data array
        x_error: <array> x-data error array
        y: <array> y-data array
        y_error: <array> y-data error array
        label: <string> data label
        color: <string> matplotlib color identifier
        xlabel: <string> x-axis label
        ylabel: <string> y-axis label
        title: <string> plot title
        out_path: <string> save path
        line: <bool> if true, plots line, else plots markers
        show: <bool> if true, plot shows, always saves
    Returns:
        None
    '''
    fig, ax = plt.subplots(
        1,
        figsize=[10, 7])
    if line:
        ax.errorbar(
            x=x,
            y=y,
            yerr=y_error,
            xerr=x_error,
            ecolor=color,
            color=color,
            marker='x',
            markersize=8,
            label=label,
            ls='-')
    else:
        ax.errorbar(
            x=x,
            y=y,
            yerr=y_error,
            xerr=x_error,
            ecolor=color,
            color=color,
            marker='x',
            markersize=8,
            label=label,
            ls='None')
    ax.grid(True)
    ax.legend(
        frameon=True,
        loc=0,
        prop={'size': 14})
    ax.set_xlabel(
        xlabel,
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_ylabel(
        ylabel,
        fontsize=14,
        fontweight='bold',
        color='black')
    ax.set_title(
        title,
        fontsize=18,
        fontweight='bold',
        color='black')
    ax.tick_params(
        axis='both',
        colors='black',
        labelsize=14)
    if show:
        plt.show()
    plt.savefig(out_path)
    fig.clf()
    plt.cla()
    plt.close(fig)


def twinx_twoy_plot(x, y1, y2,
                    label1, label2, colour1, colour2,
                    xlabel, ylabel1, ylabel2,
                    file_name, out_path,
                    line=False, show=False):
    '''
    '''
    fig, ax1 = plt.subplots(
        1,
        figsize=[10, 7])
    ax2 = ax1.twinx()
    if line:
        line1 = ax1.plot(
            x,
            y1,
            f'{colour1}',
            lw=2,
            label=label1)
        line2 = ax2.plot(
            x,
            y2,
            f'{colour2}',
            lw=2,
            label=label2)
    else:
        line1 = ax1.plot(
            x,
            y1,
            f'{colour1}.',
            markersize=4,
            label=label1)
        line2 = ax2.plot(
            x,
            y2,
            f'{colour2}.',
            markersize=4,
            label=label2)
    ax1.grid(True)
    lines = line1 + line2
    labels = [line.get_label() for line in lines]
    ax1.legend(
        lines,
        labels,
        frameon=True,
        ncol=1,
        loc=0,
        prop={'size': 14})
    ax1.set_title(
        file_name,
        fontsize=18,
        fontweight='bold')
    ax1.set_xlabel(
        xlabel,
        fontsize=14,
        fontweight='bold')
    ax1.set_ylabel(
        ylabel1,
        fontsize=14,
        fontweight='bold')
    ax2.set_ylabel(
        ylabel2,
        fontsize=14,
        fontweight='bold')
    ax1.tick_params(
        axis='x',
        labelsize=12,
        colors='black')
    ax1.tick_params(
        axis='y',
        labelsize=12,
        colors=f'{colour1}')
    ax2.tick_params(
        axis='y',
        labelsize=12,
        colors=f'{colour2}')
    if show:
        plt.show()
    plt.savefig(out_path)
    fig.clf()
    plt.cla()
    plt.close(fig)


def xy_bestfit(x, y,
               label, title,
               xlabel, ylabel,
               outpath):
    '''
    '''
    m, c = np.polyfit(x, y, 1)
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    ax.plot(x, y, 'bx', markersize=4, label=label)
    ax.plot(x, m*x+c, 'r', lw=2, label=f'y={m}x+{c}')
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def xy_exp(x, y,
           label,
           title,
           xlabel,
           ylabel,
           outpath):
    '''
    '''
    a, b = np.polyfit(x, np.log(y), 1)
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    ax.plot(x, y, 'bx', markersize=4, label=label)
    ax.plot(x, np.exp(b)*np.exp(a*x), 'r', lw=2, label=f'exp({b})*exp({a}x)')
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def xy_ylim_plot(x, y,label, title,
                 xlabel, ylabel, ylim,
                 outpath,
                 line=False):
    '''
    '''
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    if line:
        ax.plot(x, y, 'b', lw=1, label=label)
    else:
        ax.plot(x, y, 'bx', markersize=4, label=label)

    ax.legend(loc=0, prop={'size' : 10})
    ax.grid(True)
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    ax.set_ylim(ylim[0], ylim[1])
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def xy_ylim_bestfit(x, y,
                    label, title,
                    xlabel, ylabel, ylim,
                    outpath):
    '''
    '''
    m, c = np.polyfit(x, y, 1)
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    ax.plot(x, y, 'bx', markersize=4, label=label)
    ax.plot(x, m*x+c, 'r', lw=2, label=f'y={m}x+{c}')
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    ax.set_ylim(ylim[0], ylim[1])
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def xy_ylim_exp(x, y,
                label, title,
                xlabel, ylabel, ylim,
                outpath):
    '''
    '''
    a, b = np.polyfit(x, np.log(y), 1)
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    ax.plot(x, y, 'bx', markersize=4, label=label)
    ax.plot(x, np.exp(b)*np.exp(a*x), 'r', lw=2, label=f'exp({b})*exp({a}x)')
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    ax.set_ylim(ylim[0], ylim[1])
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def threexy_plot(x1, y1, x2, y2, x3, y3,
                 labels, title, xlabel, ylabel,
                 outpath, line=False):
    '''
    '''
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    if line:
        ax.plot(x1, y1, 'b', lw=2, label=labels[0])
        ax.plot(x2, y2, 'g', lw=2, label=labels[1])
        ax.plot(x3, y3, 'r', lw=2, label=labels[2])
    else:
        ax.plot(x1, y1, 'bx', markersize=4, label=labels[0])
        ax.plot(x2, y2, 'gx', markersize=4, label=labels[1])
        ax.plot(x3, y3, 'rx', markersize=4, label=labels[2])
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def threexy_bestfit_plot(x1, y1, x2, y2, x3, y3,
                         labels, title, xlabel, ylabel,
                         outpath):
    '''
    '''
    m1, c1 = np.polyfit(x1, y1, 1)
    m2, c2 = np.polyfit(x2, y2, 1)
    m3, c3 = np.polyfit(x3, y3, 1)
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    ax.plot(x1, y1, 'bx', markersize=4, label=labels[0])
    ax.plot(x1, m1*x1+c1, 'b', lw=2, label=f'y={m1}x+{c1}')
    ax.plot(x2, y2, 'gx', markersize=4, label=labels[1])
    ax.plot(x2, m2*x2+c2, 'g', lw=2, label=f'y={m2}x+{c2}')
    ax.plot(x3, y3, 'rx', markersize=4, label=labels[2])
    ax.plot(x3, m3*x3+c3, 'r', lw=2, label=f'y={m3}x+{c3}')
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def threexy_exp_plot(x1, y1, x2, y2, x3, y3,
                     labels, title, xlabel, ylabel,
                     outpath):
    '''
    '''
    a1, b1 = np.polyfit(x1, np.log(y1), 1)
    a2, b2 = np.polyfit(x2, np.log(y2), 1)
    a3, b3 = np.polyfit(x3, np.log(y3), 1)
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    ax.plot(x1, y1, 'bx', markersize=4, label=labels[0])
    ax.plot(x1, np.exp(b1)*np.exp(a1*x1), 'b',
            lw=2, label=f'exp({b1})*exp({a1}x)')
    ax.plot(x2, y2, 'gx', markersize=4, label=labels[1])
    ax.plot(x2, np.exp(b2)*np.exp(a2*x2), 'g',
            lw=2, label=f'exp({b2})*exp({a2}x)')
    ax.plot(x3, y3, 'rx', markersize=4, label=labels[2])
    ax.plot(x3, np.exp(b3)*np.exp(a3*x3), 'r',
            lw=2, label=f'exp({b3})*exp({a3}x)')
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def threexy_ylim_plot(x1, y1, x2, y2, x3, y3,
                      labels, title, xlabel, ylabel, ylim,
                      outpath, line=False):
    '''
    '''
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    if line:
        ax.plot(x1, y1, 'b', lw=2, label=labels[0])
        ax.plot(x2, y2, 'g', lw=2, label=labels[1])
        ax.plot(x3, y3, 'r', lw=2, label=labels[2])
    else:
        ax.plot(x1, y1, 'bx', markersize=4, label=labels[0])
        ax.plot(x2, y2, 'gx', markersize=4, label=labels[1])
        ax.plot(x3, y3, 'rx', markersize=4, label=labels[2])
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    ax.set_ylim(ylim[0], ylim[1])
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def threexy_bestfit_ylim_plot(x1, y1, x2, y2, x3, y3,
                              labels, title, xlabel, ylabel, ylim,
                              outpath):
    '''
    '''
    m1, c1 = np.polyfit(x1, y1, 1)
    m2, c2 = np.polyfit(x2, y2, 1)
    m3, c3 = np.polyfit(x3, y3, 1)
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    ax.plot(x1, y1, 'bx', markersize=4, label=labels[0])
    ax.plot(x1, m1*x1+c1, 'b', lw=2, label=f'y={m1}x+{c1}')
    ax.plot(x2, y2, 'gx', markersize=4, label=labels[1])
    ax.plot(x2, m2*x2+c2, 'g', lw=2, label=f'y={m2}x+{c2}')
    ax.plot(x3, y3, 'rx', markersize=4, label=labels[2])
    ax.plot(x3, m3*x3+c3, 'r', lw=2, label=f'y={m3}x+{c3}')
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    ax.set_ylim(ylim[0], ylim[1])
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)


def threexy_exp_ylim_plot(x1, y1, x2, y2, x3, y3,
                          labels, title, xlabel, ylabel, ylim,
                          outpath):
    '''
    '''
    a1, b1 = np.polyfit(x1, np.log(y1), 1)
    a2, b2 = np.polyfit(x2, np.log(y2), 1)
    a3, b3 = np.polyfit(x3, np.log(y3), 1)
    fig, ax = plt.subplots(1, 1, figsize=[10, 7])
    ax.plot(x1, y1, 'bx', markersize=4, label=labels[0])
    ax.plot(x1, np.exp(b1)*np.exp(a1*x1), 'b',
            lw=2, label=f'exp({b1})*exp({a1}x)')
    ax.plot(x2, y2, 'gx', markersize=4, label=labels[1])
    ax.plot(x2, np.exp(b2)*np.exp(a2*x2), 'g',
            lw=2, label=f'exp({b2})*exp({a2}x)')
    ax.plot(x3, y3, 'rx', markersize=4, label=labels[2])
    ax.plot(x3, np.exp(b3)*np.exp(a3*x3), 'r',
            lw=2, label=f'exp({b3})*exp({a3}x)')
    ax.grid(True)
    ax.legend(loc=0, prop={'size' : 10})
    ax.set_title(title, fontsize=18, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=14, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    ax.set_ylim(ylim[0], ylim[1])
    #plt.show()
    plt.savefig(outpath)
    fig.clf()
    plt.close(fig)
