#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "UserCenter/Inc/script.js", "siteserver")
    whatweb.recog_from_header(pluginname, "SITESERVER")


