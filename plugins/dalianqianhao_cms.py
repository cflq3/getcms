#!/usr/bin/env python
# encoding: utf-8

def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "ACTIONLOGON.APPPROCESS?mode=5", "WebUserNO")

