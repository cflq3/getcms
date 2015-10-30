#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "AspCms")
    whatweb.recog_from_file(pluginname, "Images/qq/qqkf2/kefu.js", "Kefu")


