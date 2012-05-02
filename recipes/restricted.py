from recipe import Recipe
import subprocess

class Restricted(Recipe):
    def __init__(self, user):
        super(Restricted, self).__init__(user)
        self.message('installing restricted extras')

    def execute(self):
        self.banner()
        if self.is_ok('Install restricted extras'):
            # this needs user input so we can't install via install_package
            command = 'apt-get install -y ubuntu-restricted-extras'
            subprocess.call(command, shell=True)

    def is_valid(self):
        return True
