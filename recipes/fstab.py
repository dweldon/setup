from recipe import Recipe

class Fstab(Recipe):
    def __init__(self, user):
        super(Fstab, self).__init__(user)
        self.message('editing fstab')
        self.filename = '/etc/fstab'

    def execute(self):
        self.banner()
        self.run("cp %s %s.old" % (self.filename, self.filename))

        if self.is_ok('Add tmpfs support'):
            text = "tmpfs /tmp tmpfs defaults,noatime,mode=1777 0 0"
            self.append_text(self.filename, text)

        if (self.is_success("grep '/dev/sda' " + self.filename) and
            self.is_ok('Add SSD tweaks')):
            old = 'ext4    errors=remount-ro 0'
            new = 'ext4    defaults,discard,noatime,errors=remount-ro 0'
            self.replace_text(self.filename, old, new)

    def is_valid(self):
        return True
