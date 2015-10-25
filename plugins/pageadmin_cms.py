#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "PageAdmin")
    whatweb.recog_from_file(pluginname, "e/master/master.js", "PageAdmin")

