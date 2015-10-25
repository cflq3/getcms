#!/usr/bin/env python
# encoding: utf-8

def run(whatweb, pluginname):
    whatweb.recog_from_file(pluginname, "awstats/awstats.pl?config=wellness", "AWStats")

