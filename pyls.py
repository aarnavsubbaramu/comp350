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
