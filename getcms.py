#!/usr/bin/env python
# encoding: utf-8
import sys
import web_finder

try:
    target=sys.argv[1]
    if not target.startswith('http://'):
        print ('Useage: python get_cms.py http://www.baidu.com/')
        sys.exit()

except Exception, e:
    print ('Useage: python get_cms.py http://www.baidu.com/')
else:
    res=web_finder.whatweb(target)
    if len(res.return_result())==1:
        print res.return_result().pop()
    else:
        print res.return_result()





