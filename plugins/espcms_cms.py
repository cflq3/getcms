#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "espcms")
    whatweb.recog_from_file(pluginname, "templates/wap/cn/public/footer.html", "espcms")


