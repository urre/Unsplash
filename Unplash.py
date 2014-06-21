import sublime, sublime_plugin, random, os

def insert_unsplash( kind ):
    from os.path import join
    package_path = join(sublime.packages_path(), "Unsplash")
    unpath = os.path.join(package_path, "unsplash.txt")

    with open(unpath) as f:
        lines = f.read().splitlines()
        splash = random.choice(lines)

    if kind == "tag":
        imagetag = '<img src="%s" />'% (splash)
    elif kind == "background":
        imagetag = 'background-image: url("%s") no-repeat center center'% (splash)
    else:
        imagetag = '%s'% (splash)

    view = sublime.active_window().active_view()
    edit = view.begin_edit()
    for region in view.sel():
        view.replace(edit, region, imagetag)
    view.end_edit(edit)

class InsertUnsplashCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        insert_unsplash('tag')

class InsertUnsplashUrlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        insert_unsplash('url')

class InsertUnsplashBackgroundCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        insert_unsplash('background')