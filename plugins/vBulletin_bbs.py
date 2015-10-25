#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "vbulletin")
    whatweb.recog_from_header(pluginname, "bbsessionhash")


