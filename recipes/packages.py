from recipe import Recipe

class Packages(Recipe):
    def __init__(self, user):
        super(Packages, self).__init__(user)
        self.message('installing useful packages')
        self.packages_install = ['aptitude',
                                 'build-essential',
                                 'curl',
                                 'tree',
                                 'gedit-plugins',
                                 'indicator-multiload',
                                 'libssl-dev',
                                 'meld',
                                 'ntp',
                                 'tofrodos']

        self.packages_remove = ['unity-lens-shopping',
                                'unity-scope-video-remote',
                                'unity-scope-musicstores']

    def execute(self):
        self.progress('updating all packages')
        self.run('apt-get update')
        self.run('apt-get upgrade -y')

        for package in self.packages_install:
            self.progress('installing ' + package)
            self.install_package(package)

        for package in self.packages_remove:
            self.progress('removing ' + package)
            self.remove_package(package)

    def is_valid(self):
        return True
