#!/usr/bin/env python

from recipes.node import Node
import getpass
import os

if __name__ == '__main__':
    if os.geteuid() != 0:
        Node(getpass.getuser()).download_and_install()
