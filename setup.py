#!/usr/bin/env python

import os
import sys
from recipes.examples import Examples
from recipes.packages import Packages
from recipes.bashrc import Bashrc
from recipes.python import Python
from recipes.node import Node
from recipes.gedit import Gedit
from recipes.git import Git
from recipes.fstab import Fstab
from recipes.restricted import Restricted

def check_if_root():
    if os.geteuid() != 0:
        print 'You must be root to run this script.'
        sys.exit(1)

def get_user():
    user = raw_input('What user do you wish to install for: ')
    assert os.path.exists(os.path.expanduser('~' + user))
    return user

def execute_recipe(recipe):
    recipe.execute()
    if not recipe.is_valid():
        print('ERROR: the %s recipe did not execute properly' %
              recipe.__class__.__name__)
        sys.exit(1)

if __name__ == '__main__':
    check_if_root()
    user = get_user()
    execute_recipe(Examples(user))
    execute_recipe(Packages(user))
    execute_recipe(Bashrc(user))
    execute_recipe(Node(user))
    execute_recipe(Gedit(user))
    execute_recipe(Git(user))
    execute_recipe(Fstab(user))
    execute_recipe(Restricted(user))
