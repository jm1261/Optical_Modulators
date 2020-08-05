import json


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
