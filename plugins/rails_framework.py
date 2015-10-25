#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_header(pluginname, "rails")
    whatweb.recog_from_header(pluginname, "Phusion")
    whatweb.recog_from_header(pluginname, "Webrick")



