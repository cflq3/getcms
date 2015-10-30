#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "Discuz")
    whatweb.recog_from_file(pluginname, "robots.txt", "Discuz")
    whatweb.recog_from_file(pluginname, "static/js/admincp.js","Discuz")



