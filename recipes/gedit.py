from recipe import Recipe
import os
import subprocess

class Gedit(Recipe):
    def __init__(self, user):
        super(Gedit, self).__init__(user)
        self.message('installing gedit add-ons')
        self.dir_lang = os.path.join(self.home,
            '.local/share/gtksourceview-3.0/language-specs')
        self.dir_styles = os.path.join(self.home,
            '.local/share/gtksourceview-3.0/styles')
        self.dir_tools = os.path.join(self.home, '.config/gedit/tools')
        self.filename = os.path.join(os.path.dirname(__file__),
            '../tools/run-python')

    def execute(self):
        cwd = os.getcwd()

        # create the necessary directories
        self.run('mkdir -p ' + self.dir_lang, False)
        self.run('mkdir -p ' + self.dir_tools, False)
        self.run('mkdir -p ' + self.dir_styles, False)
        self.run('cp %s %s' % (self.filename, self.dir_tools), False)

        # copy the language files
        os.chdir(self.dir_lang)
        subprocess.call('rm -f *.lang*', shell=True)
        self.wget('https://raw.github.com/LearnBoost/stylus/master/editors/gedit/styl.lang', False)
        self.wget('https://raw.github.com/lbdremy/gedit-jade/master/jade.lang', False)
        self.wget('https://raw.github.com/wavded/gedit-coffeescript/master/coffee_script.lang', False)

        #copy the style files
        os.chdir(self.dir_styles)
        subprocess.call('rm -f *.xml*', shell=True)
        self.wget('http://ideasman42-dev-scripts.googlecode.com/svn/trunk/cfg/gedit/inkpot-color-scheme.xml', False)

        os.chdir(cwd)

    def is_valid(self):
        return (os.path.exists(os.path.join(self.dir_styles, 'inkpot-color-scheme.xml')) and
                os.path.exists(os.path.join(self.dir_tools, 'run-python')) and
                os.path.exists(os.path.join(self.dir_lang, 'styl.lang')) and
                os.path.exists(os.path.join(self.dir_lang, 'jade.lang')) and
                os.path.exists(os.path.join(self.dir_lang, 'coffee_script.lang')))
