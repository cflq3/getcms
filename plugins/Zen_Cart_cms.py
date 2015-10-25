#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "Zen Cart")
    whatweb.recog_from_header(pluginname, "zenid")


