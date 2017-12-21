from pathlib import Path


def get_files(extension, path, recursive=True):
    is_Path = True
    if isinstance(path, str):
        is_Path = False
        path = Path(path)
    if recursive:
        extension = '**/'+extension
    found = list(path.glob(extension))
    if is_Path:
        return found
    return [file_path._str for file_path in found]

