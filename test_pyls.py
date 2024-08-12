import os
import pytest
from pyls import list_directory, list_directory_classified, list_directory_detailed

def test_list_directory():
    os.mkdir('testdir')
    with open('testfile.txt', 'w') as f:
        f.write('test')
    assert 'testdir' in list_directory()
    assert 'testfile.txt' in list_directory()

def test_list_directory_classified():
    assert 'testdir/' in list_directory_classified()
    assert 'testfile.txt' in list_directory_classified()

def test_list_directory_detailed():
    assert 'testdir' in list_directory_detailed()
    assert 'testfile.txt' in list_directory_detailed()

if __name__ == "__main__":
    pytest.main()
