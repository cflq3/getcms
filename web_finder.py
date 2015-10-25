#!/usr/bin/env python
# encoding: utf-8

import os
import requests

RESULT_CMS=set()
RESULT_APP=set()
RESULT_FRAMEWORK=set()
RESULT_OTHER=set()


class whatweb():
    def __init__(self, target=''):
        self.target=target
        r=requests.get(target)
        self.headers=r.headers
        self.content=r.content
        self.loadplugins()

    def loadplugins(self):
        for filename in os.listdir("plugins"):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue
            self.runplugin(filename)

    def runplugin(self, filename):
        pluginname = os.path.splitext(filename)[0]
        plugin=__import__("plugins."+ pluginname, fromlist=[pluginname])
        plugin.run(self, pluginname)

    def recog_from_header(self, pluginname, plugin_header):
        headers=self.headers
        for (key, value) in headers.items():
            if plugin_header in value:
               # print pluginname
                if pluginname.endswith('cms'):
                    RESULT_CMS.add(pluginname)
                elif pluginname.endswith('framework'):
                    RESULT_FRAMEWORK.add(pluginname)
                elif pluginname.endswith('app'):
                    RESULT_APP.add(pluginname)
            else:
                RESULT_OTHER.add(pluginname)

    def recog_from_content(self, pluginname, plugin_content):
        if plugin_content in self.content:
            # print pluginname
            if pluginname.endswith('cms'):
                RESULT_CMS.add(pluginname)
            elif pluginname.endswith('framework'):
                RESULT_FRAMEWORK.add(pluginname)
            elif pluginname.endswith('app'):
                RESULT_APP.add(pluginname)
            else:
                RESULT_OTHER.add(pluginname)
        else:
            pass

    def recog_from_file(self, pluginname, plugin_file, file):
        f=requests.get(self.target+ plugin_file)
        code=f.status_code
        if code==200:
            if file in f.content:
                # print pluginname
                if pluginname.endswith('cms'):
                    RESULT_CMS.add(pluginname)
                elif pluginname.endswith('server'):
                    RESULT_FRAMEWORK.add(pluginname)
                elif pluginname.endswith('app'):
                    RESULT_APP.add(pluginname)
            else:
                RESULT_OTHER.add(pluginname)
        else:
            pass
    def return_result(self):
        return  RESULT_CMS
        # print ('FRAMEWORK:'), RESULT_FRAMEWORK
        # print ('APP:'), RESULT_APP
        # print ('OTHER:'), RESULT_OTHER


if __name__=="__main__":

    res=whatweb('http://www.baidu.com')
    print ('CMS:'), RESULT_CMS
    # print ('FRAMEWORK:'+RESULT_FRAMEWORK)
    # print ('APP:'+RESULT_APP)
    # print ('OTHER:'+RESULT_OTHER)








