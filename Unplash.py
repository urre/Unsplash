import sublime, sublime_plugin, random, os

class InsertUnsplashCommand(sublime_plugin.TextCommand):
    def run(self, edit, args):
        from os.path import join
        package_path = join(sublime.packages_path(), "Unsplash")
        unpath = os.path.join(package_path, "unsplash.txt")

        with open(unpath) as f:
            lines = f.read().splitlines()
            splash = random.choice(lines)

        if args['type'] == "tag":
            imagetag = '<img src="%s">'% (splash)
        elif args['type'] == "background":
            imagetag = 'background-image: url("%s") no-repeat center center'% (splash)
        else:
            imagetag = '%s'% (splash)

        for region in self.view.sel():
            self.view.replace(edit, region, imagetag)

class InsertUnsplashTagCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_unsplash", {"args":{'type':'tag'}})


class InsertUnsplashUrlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_unsplash", {"args":{'type':'url'}})


class InsertUnsplashBackgroundCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_unsplash", {"args":{'type':'background'}})