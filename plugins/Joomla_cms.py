#!/usr/bin/env python
# encoding: utf-8


def run(whatweb, pluginname):
    whatweb.recog_from_content(pluginname, "Joomla")
    whatweb.recog_from_file(pluginname, "htaccess.txt","Joomla")
    whatweb.recog_from_file(pluginname, "components/com_mailto/views/sent/metadata.xml", "joomla")

