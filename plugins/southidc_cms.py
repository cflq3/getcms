#!/usr/bin/env python
# encoding: utf-8

def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "Script/FocusSlide.js", "southidc")
    whatweb.recog_from_content(pluginname, "southidc")


