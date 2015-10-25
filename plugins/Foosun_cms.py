#!/usr/bin/env python
# encoding: utf-8

def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "sysImages/css/PagesCSS.css", "foosun")
    whatweb.recog_from_file(pluginname, "Tags.html", "Foosun")

