#!/usr/bin/env python
# encoding: utf-8

def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "robots.txt", "FineCMS")
    whatweb.recog_from_file(pluginname, "member/statics/js/dayrui.js", "Dayrui")


