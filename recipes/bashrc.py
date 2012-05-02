from recipe import Recipe
import os.path

class Bashrc(Recipe):
    def __init__(self, user):
        super(Bashrc, self).__init__(user)
        self.filename = '.bashrc'
        self.message('editing ' + self.filename)
        self.filename_user = os.path.join(self.home, self.filename)
        self.filename_root = os.path.join('/root', self.filename)

    def execute(self):
        self.update_bashrc(self.filename_root, True)
        self.update_bashrc(self.filename_user, False)

    def is_valid(self):
        return (self.is_success('grep nano ' + self.filename_user) and
                self.is_success('grep nano ' + self.filename_root))

    def update_bashrc(self, filename, as_root=True):
      text_map = dict({"alias ll='ls -alF'": "alias ll='ls -l'",
                       "alias la='ls -A'": "alias la='ls -lA'",
                       "alias l='ls -CF'": "alias l='ls -C'"})

      copy_command = "cp %s %s.old" % (filename, filename)
      self.run(copy_command, as_root)

      for old, new in text_map.items():
        self.replace_text(filename, old, new, as_root)

      self.append_text(filename)
      self.append_text(filename, '# editor aliases')
      self.append_text(filename, "alias n='nano -w'")

      if as_root is False:
          self.append_text(filename, "alias g='gedit'")
          self.append_text(filename)
