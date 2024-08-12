import os

def list_directory():
    """List files and directories in the current working directory."""
    files = os.listdir('.')
    for file in files:
        print(file)

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    if not args:
        list_directory()

def list_directory_classified():
    """List files and directories in the current working directory with classification."""
    files = os.listdir('.')
    for file in files:
        if os.path.isdir(file):
            print(f"{file}/")
        elif os.access(file, os.X_OK):
            print(f"{file}*")
        else:
            print(file)

if __name__ == "__main__":
    if '-F' in args:
        list_directory_classified()
    else:
        list_directory()

import time

def list_directory_detailed():
    """List files and directories with details (last modified date, size)."""
    files = os.listdir('.')
    for file in files:
        stats = os.stat(file)
        modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
        size = stats.st_size if os.path.isfile(file) else 0
        print(f"{modified_time} {size:10} {file}")

if __name__ == "__main__":
    if '-l' in args:
        list_directory_detailed()
    elif '-F' in args:
        list_directory_classified()
    else:
        list_directory()

def print_help():
    """Print help information."""
    help_text = """Usage: pyls [options]
Options:
  -F       Append indicator (one of */) to entries
  -l       Use a long listing format
  -h, --help  Display this help and exit
    """
    print(help_text)

if __name__ == "__main__":
    if '-h' in args or '--help' in args:
        print_help()
    elif '-l' in args and '-F' in args:
        list_directory_detailed_classified()
    elif '-l' in args:
        list_directory_detailed()
    elif '-F' in args:
        list_directory_classified()
    else:
        list_directory()
