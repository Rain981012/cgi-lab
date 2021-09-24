#!/usr/bin/env python3
import os, json
print("Content - type:text/html\r\n\r\n")
print("<title> Test CGI </title>")
print("<p>Hello World!</p>")

#Q1
print(os.environ)
json_object = json.dumps(dict(os.environ), indent=4)

###Q2
for param in os.environ.keys():
    if (param == "QUERY_STRING"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

##Q3:
for param in os.environ.keys():
    if(param == "HTTP_USER_AGENT"):
        print("<b>%20s</b>" % (param, os.environ[param]))