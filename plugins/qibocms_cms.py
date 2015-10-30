#!/usr/bin/env python
# encoding: utf-8

def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "admin/template/article_more/config.htm", "width")
    whatweb.recog_from_file(pluginname, "robots.txt", "qibo")


