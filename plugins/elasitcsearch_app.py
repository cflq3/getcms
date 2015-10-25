#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_header(pluginname, "application/json")
    whatweb.recog_from_content(pluginname, "build_hash")


