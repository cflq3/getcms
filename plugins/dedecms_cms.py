#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "dedecms")
    whatweb.recog_from_file(pluginname, "templets/default/style/dedecms.css", "DedeCMS")


