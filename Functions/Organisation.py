import os
import datetime


def datetime_string():
    '''
    Grab current date and time and format a string for file naming.
    Args:
        none
    Returns:
        string: <string> YearMonthDayHourMinute string
    '''
    date_time = datetime.datetime.now()
    string = (f'{date_time.strftime("%Y")}'
              f'{date_time.strftime("%m")}'
              f'{date_time.strftime("%d")}'
              f'{date_time.strftime("%H")}'
              f'{date_time.strftime("%M")}')
    return string


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


def check_dir_exists(dir_path):
    '''
    Check to see if a directory path exists, and if not create one
    Args:
        dir_path: <string> directory path
    '''
    if os.path.isdir(dir_path) is False:
        os.mkdir(dir_path)
