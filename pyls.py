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
