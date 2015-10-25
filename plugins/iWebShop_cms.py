#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "iWebShop")
    whatweb.recog_from_header(pluginname, "iweb_safecode")


