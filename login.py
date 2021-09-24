#!/usr/bin/env python3


import cgi, cgitb
from os import environ
import os
import secret
from http import cookies
import templates

#create instance of field
form = cgi.FieldStorage()

#Get data from fields
username = form.getvalue('username')
password = form.getvalue('password')
print("Content_type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI program</title>")
print("</head>")
print("<body>")
print("<p><b>Username<\b> %s <b>password</b> %s</p>" % (username,password))
print("</body>")
print("</html>")

if username == secret.username and password == secret.password:
    C = cookies.SimpleCookie()
    C["Username"] = username
    C["Password"] = password
    
    print(C['Username'])


    cookie_load = os.environ.get('HTTP_COOKIE')
    C.load(cookie_load)

    c_username = None
    c_password = None
    key = C["Username"].value
    password = C["Password"].value

    print(templates.secret_page(key, password))

    if C.get("Username"):
        c_username = C.get("Username").value
    if C.get("Password"):
        c_password = C.get("Password").value
else: 
    templates.after_login_incorrect()