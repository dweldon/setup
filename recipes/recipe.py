import getpass
import os
import subprocess
import shlex

class Recipe(object):
    temp = '/tmp'

    def __init__(self, user):
        self.user = user
        self.home = os.path.expanduser('~' + user)
        assert os.path.exists(self.home)

    def execute(self):
        raise NotImplementedError()

    def is_valid(self):
        raise NotImplementedError()

    def banner(self):
        print '****************************************************************'

    def message(self, string):
        print '- ' + string

    def progress(self, string):
        print '\t* ' + string

    def run(self, command, as_root=True):
        fnull = open(os.devnull, 'w')
        parts = shlex.split(command)
        args = parts if as_root else ['sudo', '-u', self.user] + parts
        result = subprocess.call(args, stdout=fnull, stderr=fnull)
        fnull.close()
        return result

    def is_success(self, command, as_root=True):
        return self.run(command, as_root) == 0

    def install_package(self, name):
        return self.run('apt-get install -y ' + name)

    def replace_text(self, filename, old, new, as_root=True):
        command = 'sed -i "s/%s/%s/" %s' % (old, new, filename)
        self.run(command, as_root)

    def append_text(self, filename, text=''):
        with open(filename, "a") as f:
            f.write(text + '\n')

    def wget(self, url, as_root=True):
        command = "wget -q --no-check-certificate " + url
        return self.run(command, as_root)

    def is_ok(self, string):
        result = raw_input(string + '? [y/n]\n').strip().lower()
        if result == 'y': return True
        if result == 'n': return False
        return self.is_ok(string)

    def __repr__(self):
        return '%s: user=%r, home=%r' % \
               (self.__class__.__name__, self.user, self.home)
