#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_header(pluginname, "WS CDN Server")
    whatweb.recog_from_header(pluginname, "Cdn Cache Server")


