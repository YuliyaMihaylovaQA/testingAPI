import os.path


def get_current_path(file_name: str):
    current_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_path, file_name)