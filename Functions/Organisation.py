import os
import json
import tkinter as tk
from tkinter import filedialog


def get_config(config_path):
    '''
    Extract user variables from JSON formatted configuration file
    Args:
        config_path: <string> config file path
    Returns:
        <dict> of user variables, all values as strings
    '''
    if config_path:
        with open(config_path, 'r') as f:
            return json.load(f)


def get_filename(file_path):
    '''
    Takes a file name path and splits on '/' to obtain only the file name.
    Splits the file name from extension and returns just the user asigned
    file name as a string.
    Args:
        file_path: <string> path to file
    Returns:
        file_name: <string> file name string without path or extension
    '''
    return os.path.splitext(os.path.basename(file_path))[0]


def file_sort(dir_path):
    '''
    Numerically sort a directory containing a combination of string file names
    and numerical file names
    Args:
        dir_path: <string> directory path
    Returns:
        sorted_array: <array> contents of dir_path sorted numerically
    '''
    return sorted(os.listdir(dir_path))


def extract_files(dir_path,
                  file_string):
    '''
    Stack file names in a directory into an array. Returns data files array.
    Args:
        dir_path: <string> directory path
        file_string: <string> within desired file names
    Returns:
        array: <array> containing sorted and selected file name strings
    '''
    dir_list = file_sort(dir_path)
    return [a for a in dir_list if file_string in a]


def find_files(dir_path,
               file_string):
    '''
    Find files creates two arrays, one containing all the data files and one
    with all the plotted files from a given directory path. Find files assumes
    all output plots are saved with .png extension.
    Args:
        dir_path: <string> path to directory
        file_string: <string> within desired file names
    Returns:
        data_files: <array> array of all files within directory with given file
                    string
        plot_files: <array> array of all files within directory already plotted
    '''
    data_files = extract_files(dir_path=dir_path,
                               file_string=file_string)
    plot_files = extract_files(dir_path=dir_path,
                               file_string='.png')
    return data_files, plot_files


def find_path(default,
              dir_path=False,
              file_path=False,
              file_type=False):
    '''
    Find path is an interactive path finding tool. Using tkinter, find path
    allows the user to select a directory or file path (depending on args)
    and returns the path to that directory or file. If no option is entered
    the function returns a reminder string.
    Args:
        default: <string> path to default directory for interactive window
        dir_path: <bool> if True, find path looks for a directory path
        file_path: <bool> if True, find path looks for a file path
        file_type: <string> if file_path true, file_type must be of the form
                   "[(file type, *.file extension)]"
    Returns:
        path: <string> string to desired object, or reminder string if no input
    '''
    root = tk.Tk()
    root.withdraw()
    path = 'Please Select dir_path or file_path'
    if dir_path:
        path = filedialog.askdirectory(initialdir=default,
                                       title='Select a Directory')
    if file_path:
        path = filedialog.askopenfilename(initialdir=default,
                                          filetypes=file_type,
                                          title='Select a File')
    return path


def save_path(file_type,
              default_name):
    '''
    Save path is an interactive path finding tool. Using tkinter, save path
    allows the user to select a file path to save out a file and returns the
    path for other python functions to save.
    Args:
        file_type: <string> file type must be of the form "[(file type,
                   *.file extension)]" and will automatically apply the
                   selected file extension
        default_name: <string> the default file name that appears in the save
                      window, typically the original file name but with a png
                      extension
    Returns:
        path: <string> selected file path
    '''
    root = tk.Tk()
    root.withdraw()
    path = filedialog.asksaveasfilename(filetypes=file_type,
                                        defaultextension=file_type,
                                        title='Save As',
                                        initialfile=default_name)
    return path


def check_dir_exists(dir_path):
    '''
    Check to see if a directory path exists, and if not create one
    Args:
        dir_path: <string> directory path
    '''
    if os.path.isdir(dir_path) is False:
        os.mkdir(dir_path)


def dump_json(out_path, dictionary):
    '''
    Add a dictionary to a json dictionary.
    Args:
        out_path: <string> path to file, including file name and extension
        dictionary: <dictionary> python dictionary to put in file
    '''
    with open(out_path, 'w') as outfile:
        json.dump(dictionary, outfile)


def get_sample_name(file, index):
    '''
    '''
    file_split = file.split('_')
    sample_name = file_split[index]
    return sample_name
