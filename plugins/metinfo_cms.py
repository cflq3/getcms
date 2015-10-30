#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "metinfo")
    whatweb.recog_from_file(pluginname, "job/templates/met/css/style.css", "member")

