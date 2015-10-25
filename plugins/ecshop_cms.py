#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_header(pluginname, "ECS_ID")
    whatweb.recog_from_content(pluginname, "ecshop")
    whatweb.recog_from_file(pluginname, "robots.txt", "cycle_image.php")


