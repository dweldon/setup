from recipe import Recipe
import os

class Python(Recipe):
    def __init__(self, user):
        super(Python, self).__init__(user)
        self.message('setting up python')
        self.envdir = os.path.join(self.home, '.virtualenvs')

    def execute(self):
        for package in ['python-dev', 'python-pip']:
            self.progress('installing ' + package)
            self.install_package(package)

        self.progress('upgrading pip')
        self.run('pip install --upgrade pip')

        for package in ['virtualenv', 'virtualenvwrapper']:
            self.progress('installing ' + package)
            self.run('pip install ' + package)

        self.run('mkdir ' + self.envdir, False)
        self.append_text(os.path.join(self.home, '.bashrc'),
                         'source /usr/local/bin/virtualenvwrapper.sh')

    def is_valid(self):
        return (os.path.exists(self.envdir) and
                self.is_success('which virtualenv'))
