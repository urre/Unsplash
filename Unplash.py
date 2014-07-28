import sublime, sublime_plugin, random, os, json
import xml.etree.ElementTree as ET

class InsertUnsplashCommand(sublime_plugin.TextCommand):
    def run(self, edit, args):

        sublimeVersion = int(sublime.version())
        st2 = False
        st3 = False

        if sublimeVersion < 3000:
            st2 = True
            from urllib import urlopen
        else:
            st3 = True
            import urllib.request

        tumblr_name = 'unsplash'
        api_endpoint = 'http://unsplash.tumblr.com/api/read?num=100?type=photo'
        photoUrls = []
        settings = sublime.load_settings("Unsplash.sublime-settings")
        imgWidth = settings.get("imgWidth", 10)

        if st2:
            resp = urlopen(api_endpoint)
        else:
            resp = urllib.request.urlopen(api_endpoint)

        content = resp.read()
        tree = ET.fromstring(content)
        post_tags = tree.findall(".//post")
        post_count = len(post_tags)
        for post_tag in post_tags:

            for photo_tag in post_tag.findall(".//photo-url"):
                if photo_tag.attrib['max-width'] == str(imgWidth):
                    photoUrl = photo_tag.text
                    photoUrls.append(photoUrl)

        splash = random.choice(photoUrls)

        if args['type'] == "tag":
            imagetag = '<img src="%s">'% (splash)
        elif args['type'] == "background":
            imagetag = 'background: url("%s") no-repeat center center'% (splash)
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