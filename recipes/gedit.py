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
        self.dir_plugins = os.path.join(self.home, '.local/share/gedit/plugins')
        self.filename = os.path.join(os.path.dirname(__file__), '../tools/run')

    def execute(self):
        cwd = os.getcwd()

        # create the necessary directories
        self.run('mkdir -p ' + self.dir_lang, False)
        self.run('mkdir -p ' + self.dir_tools, False)
        self.run('mkdir -p ' + self.dir_styles, False)
        self.run('mkdir -p ' + self.dir_plugins, False)
        self.run('cp %s %s' % (self.filename, self.dir_tools), False)

        # copy the language files
        os.chdir(self.dir_lang)
        subprocess.call('rm -f *.lang*', shell=True)
        self.wget('https://raw.github.com/LearnBoost/stylus/master/editors/gedit/styl.lang', False)
        self.wget('https://raw.github.com/lbdremy/gedit-jade/master/jade.lang', False)
        self.wget('https://raw.github.com/wavded/gedit-coffeescript/master/coffee_script.lang', False)

        # copy the style files
        os.chdir(self.dir_styles)
        subprocess.call('rm -f *.xml*', shell=True)
        self.wget('http://ideasman42-dev-scripts.googlecode.com/svn/trunk/cfg/gedit/inkpot-color-scheme.xml', False)
        self.wget('https://raw.github.com/wavded/gedit-coffeescript/master/rubycius-mod.xml', False)

        # copy the plugins
        os.chdir(self.dir_plugins)
        subprocess.call('rm -f *.p*', shell=True)
        self.wget('http://git.slashdev.ca/gedit-autotab/snapshot/gedit-autotab-gedit3.tar.gz', False)
        self.run('tar xzf gedit-autotab-gedit3.tar.gz', False)
        subprocess.call('cp gedit-autotab-gedit3/*.p* .', shell=True)
        subprocess.call('rm -rf gedit-autotab-gedit3*', shell=True)

        os.chdir(cwd)

    def is_valid(self):
        return (os.path.exists(os.path.join(self.dir_styles, 'inkpot-color-scheme.xml')) and
                os.path.exists(os.path.join(self.dir_styles, 'rubycius-mod.xml')) and
                os.path.exists(os.path.join(self.dir_tools, 'run')) and
                os.path.exists(os.path.join(self.dir_lang, 'styl.lang')) and
                os.path.exists(os.path.join(self.dir_lang, 'jade.lang')) and
                os.path.exists(os.path.join(self.dir_lang, 'coffee_script.lang')))
