import os

def read_file(file_path):
    """Reads the content of a file and returns it."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def file_exists(file_path):
    """Checks if a file exists."""
    return os.path.isfile(file_path)