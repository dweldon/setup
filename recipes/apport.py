from recipe import Recipe

class Apport(Recipe):
    def __init__(self, user):
        super(Apport, self).__init__(user)
        self.message('disabling apport')
        self.filename = '/etc/default/apport'
        self.old_text = 'enabled=1'
        self.new_text = 'enabled=0'

    def execute(self):
        self.replace_text(self.filename, self.old_text, self.new_text)

    def is_valid(self):
        return self.is_success('grep %s %s' % (self.new_text, self.filename))
