#! /usr/local/bin/python2.7
# -*- coding: utf-8 -*- #

import urllib2
import urllib
import cookielib
import NrzDataStorage

def getPage(url):
	bufferedHTML = ""
	try:
		cookie_jar = cookielib.LWPCookieJar()
		cookie = urllib2.HTTPCookieProcessor(cookie_jar)
		opener = urllib2.build_opener(cookie)
		req = urllib2.Request(url,urllib.urlencode({}),{})
		res = opener.open(req)
		bufferedHTML = res.read()

	except urllib2.URLError:
		return -1
	except urllib2.HTTPError:
		return -1

	return bufferedHTML
