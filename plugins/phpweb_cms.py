#!/usr/bin/env python
# encoding: utf-8

def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "page/html/?1.html", "fontZoom")

