#!/usr/bin/env python

import requests
import sys
import optparse

def poke(url, params="", action="GET", display=False, status_code=False):
	if (action == "GET"):
		r = requests.get(url)
	elif (action == "POST"):
		r = requests.post(url, params)
	
	if (display):
		print r.text
	if (status_code):
		print r.status_code

parser = optparse.OptionParser(version="v0.0")
parser.add_option("-u", action="store", dest="url", help="target url")
parser.add_option("-g", action="store_true",dest="get", default=True, help="send a GET request (default)")
parser.add_option("-p", action="store_true",dest="post", default=False, help="send a POST request")
# params
parser.add_option("-a", action="store", dest="post_params", help="POST params")
parser.add_option("-d", action="store_true",dest="display", default=False, help="display output of request")
parser.add_option("-s", action="store_true",dest="statuscode", default=False, help="display response status code")
(options,args) = parser.parse_args()

if not options.url:
	print "Need a URL to connect to."
	sys.exit(-1)

if (options.post and options.get):
	options.get = False

if (options.get == True) and options.url:
	#print "GET %s" % options.url
	poke(options.url, "", "GET", options.display, options.statuscode)
elif options.post and options.url:
	#print "POST %s?%s" % (options.url, options.post_params)
	poke(options.url, options.post_params, "POST", options.display, options.statuscode)

#url = sys.argv[1]
#r = requests.get(url)
#print r.status_code
