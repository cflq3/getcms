#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_header(pluginname, "Microsoft-IIS")
    whatweb.recog_from_header(pluginname, "X-Powered-By: WAF/2.0")

