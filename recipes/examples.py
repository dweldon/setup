from recipe import Recipe
import os.path

class Examples(Recipe):
    def __init__(self, user):
        super(Examples, self).__init__(user)
        self.message('unlinking examples')
        self.filename = os.path.join(self.home, 'examples.desktop')

    def execute(self):
        self.run('unlink ' + self.filename)

    def is_valid(self):
        return not os.path.exists(self.filename)
