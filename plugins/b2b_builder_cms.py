#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "B2Bbuilder")
    whatweb.recog_from_file(pluginname, "admin/", "B2Bbuilder")


