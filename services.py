#!/usr/bin/python

import cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

service_data=data.getvalue('s')

if service_data == "ss" :
     print ('<meta http-equiv="Refresh" content="0; url=http://127.0.0.1/saas.html">')

elif service_data == "sts" :
     print ('<meta http-equiv="Refresh" content="0; url=http://127.0.0.1/staas.html">')
elif service_data == "ps" :
     print ('<meta http-equiv="Refresh" content="0; url=http://127.0.0.1/paas.html">')

elif service_data == "is" :
     print ('<meta http-equiv="Refresh" content="0; url=http://127.0.0.1/iaas.html">')

else :
     print ('<meta http-equiv="Refresh" content="0; url=http://127.0.0.1/services.html">')


