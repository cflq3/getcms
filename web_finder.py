#!/usr/bin/env python
# encoding: utf-8

from gevent import monkey
from gevent import Greenlet
monkey.patch_all()
import gevent
from gevent.queue import Queue
import os
import requests
import sys
sys.setrecursionlimit(10000)

tasks=Queue()
RESULT_CMS=set()
RESULT_APP=set()
RESULT_FRAMEWORK=set()
RESULT_OTHER=set()


class whatweb(Greenlet):
    def __init__(self, target=''):
        Greenlet.__init__(self)
        self.target=target
        r=requests.get(target)
        self.headers=r.headers
        self.content=r.content

        gevent.spawn(self.loadplugins).join()

        gevent.joinall([
            gevent.spawn(self.runplugin, '1'),
            gevent.spawn(self.runplugin, '2'),
            gevent.spawn(self.runplugin, '3'),
            gevent.spawn(self.runplugin, '4'),
            gevent.spawn(self.runplugin, '5'),
            gevent.spawn(self.runplugin, '6'),
            gevent.spawn(self.runplugin, '7'),
            gevent.spawn(self.runplugin, '8'),
            gevent.spawn(self.runplugin, '9'),
            gevent.spawn(self.runplugin, '10'),

        ])

    def loadplugins(self):
        for filename in os.listdir("plugins"):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue
            tasks.put_nowait(filename)


    def runplugin(self, number):
        while not tasks.empty():
            task=tasks.get()

            pluginname = os.path.splitext(task)[0]
            plugin=__import__("plugins."+ pluginname, fromlist=[pluginname])
            plugin.run(self, pluginname)
            gevent.sleep(0)

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
    def return_result(self):
        return  RESULT_CMS

        # print ('FRAMEWORK:'), RESULT_FRAMEWORK
        # print ('APP:'), RESULT_APP
        # print ('OTHER:'), RESULT_OTHER


if __name__=="__main__":
    res=whatweb('http://www.baidu.com/')
    #res=whatweb('http://www.baidu.com')
    print ('CMS:'), res.return_result()
    # print ('FRAMEWORK:'+RESULT_FRAMEWORK)
    # print ('APP:'+RESULT_APP)
    # print ('OTHER:'+RESULT_OTHER)








