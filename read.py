#!/usr/bin/env python

from config import Config
import os
import urllib2

try:
    import json
except:
    import simplejson as json

print "Content-type: application/json\n"

# Get Query Parameters
try:
    query_string = os.getenv("QUERY_STRING")
    query_pairs = query_string.strip().split('&')
    for p in query_pairs:
        query_params[p.split('=')[0]] = p.split('=')[1]
except Exception:
    pass

# Get Page to display
url = ""
try:
    url = int(query_params['url'])
except Exception:
    pass

# Load API info
config = Config()
parser_url = "https://readability.com"
parser_path = "/api/content/v1/parser"
query_url = "?url="
query_token = "&token="
request_url = "{}{}{}{}{}{}".format(parser_url,
        parser_path,
        query_url,
        url,
        query_token,
        config.get_api_key())
print request_url
contents = urllib2.urlopen(request_url).read()
print json.dumps(contents)
