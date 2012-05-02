#!/usr/bin/env python

from recipes.gedit import Gedit
from setup import execute_recipe
import getpass
import os

if __name__ == '__main__':
    if os.geteuid() != 0:
        execute_recipe(Gedit(getpass.getuser()))
