#!usr/bin/env python
#coding :utf-8

import time
from WebRender import WebRender

class CHumanoidBrowser:
    def __init__(self):
        ''''''
        self.url = ''

    def getPage(self, url, WebRender):
        self.url = url
        WebRender.get(url)





def main(url):
    mBrowser = CHumanoidBrowser()
    mWebRender = WebRender.CWebRender()
    mBrowser.getPage(url, mWebRender)



if __name__ == '__main__':
    url = ''
    main(url)

