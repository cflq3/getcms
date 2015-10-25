#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "phpwind")
    whatweb.recog_from_file(pluginname, "js/pw_ajax.js", "function")

