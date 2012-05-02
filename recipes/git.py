from recipe import Recipe
import os.path

class Git(Recipe):
    def __init__(self, user):
        super(Git, self).__init__(user)
        self.message('installing git')

    def execute(self):
        self.install_package('git')
        self.banner()
        name = raw_input('What is your full name?\n').strip().lower()
        email = raw_input('What is your email?\n').strip().lower()
        self.run('git config --global user.name "%s"' % name, False)
        self.run('git config --global user.email "%s"' % email, False)
        self.run('git config --global color.ui auto', False)
        self.run('git config --global push.default matching', False)
        self.run('git config --global alias.hist \'log --pretty=format:"%C(yellow)%h%C(reset) %ad %C(magenta)[%an]%C(reset) %C(green)%s%C(reset)%d" --graph --date=short\'', False)

    def is_valid(self):
        return os.path.exists(os.path.join(self.home, '.gitconfig'))
