#!/usr/bin/env python

from config import Config
import urllib2
import os
import urlparse
try:
    import json
except:
    import simplejson as json

print "Content-type: application/json\n"
#print "Content-type: text/html\n"

try:
    url = os.environ['HTTP_HOST']
    uri = os.environ['REQUEST_URI']
    parsed = urlparse.urlparse(url+uri)
    url = urlparse.parse_qs(parsed.query)['url'][0]
except Exception:
    url = "http://read.tomasino.org/index.html"
    pass

# Load API info
config = Config()
parser_url = "http://readability.com/api/content/v1/parser?url="
query_token = "&token="
request_url = "{}{}{}{}".format(parser_url,
        url,
        query_token,
        config.get_api_key())
try:
    contents = urllib2.urlopen(request_url).read()
except Exception:
    url = "http://read.tomasino.org/index.html"
    request_url = "{}{}{}{}".format(parser_url,
            url,
            query_token,
            config.get_api_key())
    contents = urllib2.urlopen(request_url).read()

print contents
