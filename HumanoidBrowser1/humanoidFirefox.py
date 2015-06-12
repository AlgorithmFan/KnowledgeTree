#!usr/bin/env python
#coding:utf-8

import time
from WebRender import WebRender

class CHumanoidBrowser:
    def __init__(self):
        ''''''
        self.url = ''

    def getPage(self, url, WebRender):
        self.url = url
        WebRender.get(url)

    def search(self, WebRender, text):
        # '''执行搜索功能'''
        try:
            if len(text) == 0:
                return True
            search = WebRender.find_element_by_class_name("form-control")
            search.send_keys(text)
            button = WebRender.find_element_by_xpath("//input[@class='btn btn-default']")
            button.click()
        except:
            return False



def main(url):
    mBrowser = CHumanoidBrowser()
    mWebRender = WebRender.CWebRender()
    mBrowser.getPage(url, mWebRender)
    # fp = open('search.txt')
    # text = fp.readline()
    # fp.close()
    text = u'西安'
    mBrowser.search(mWebRender, text)
    mWebRender.closeUrl()



if __name__ == '__main__':
    url = 'http://know.bkw100.com'
    main(url)

