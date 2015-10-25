#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "ks_inc")
    whatweb.recog_from_file(pluginname, "KS_Inc/ajax.js", "KesionCMS")

