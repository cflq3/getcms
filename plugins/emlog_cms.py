#!/usr/bin/env python
# encoding: utf-8

def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "include/lib/js/imgareaselect/jquery.imgareaselect.js", "emlog")
    whatweb.recog_from_file(pluginname, "wlwmanifest.xml", "emlog")

