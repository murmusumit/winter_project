#!/usr/bin/python

import cgi

print "Content-type:text/html"
print ""

webdata=cgi.FieldStorage()

user=webdata.getvalue('u')
password=webdata.getvalue('p')


if user == 'sumit' and password == 'redhat' :
      print ('<meta http-equiv="Refresh" content ="0; url=http://localhost/services.html">')
else :
      print ('<meta http-equiv="Refresh" content ="0; url=http://localhost/index.html">')

