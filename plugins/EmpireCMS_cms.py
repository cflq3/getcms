#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "EmpireCMS")
    whatweb.recog_from_file(pluginname, "e/member/login/loginjs.php", "document")
    whatweb.recog_from_file(pluginname, "e/tool/feedback/temp/test.txt", "EmpireCMS")


