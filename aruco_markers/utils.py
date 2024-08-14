import os
from os import remove
from os import listdir
from os.path import isdir, isfile
from os.path import join as join_path

# Solution adapted from Stack Overflow.
# URL: https://stackoverflow.com/questions/14742064/python-os-environhome-works-on-idle-but-not-in-a-script
homedir = os.path.expanduser('~')


def mkdir(path, dirname):
    """Join the paths, and if the directory does not already exist then it is created."""
    fullpath = join_path(path, dirname)
    if not isdir(fullpath):
        os.mkdir(fullpath)
        print("Created", fullpath)
    return fullpath
