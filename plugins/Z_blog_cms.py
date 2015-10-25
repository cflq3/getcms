#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "script/common.js", "Z-Blog")
    whatweb.recog_from_content(pluginname, "zb_users")


