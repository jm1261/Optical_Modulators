import os
import numpy as np
import json
import datetime


def get_config(file_path):
    '''
    Extract user variables from JSON formatted configuration file.
    Args:
        file_path: <string> config file path
    Returns:
        <dict> user variables in dictionary
    '''
    if file_path:
        with open(file_path, 'r') as f:
            return json.load(f)


def write_config(file_path, data):
    '''
    Write user variables to JSON formatted configuration file.
    Args:
        file_path: <string> config file path
        data: <dict> dictionary user values
    Returns:
        none
    '''
    if file_path:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)


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
