#!/usr/bin/python

import cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

service_data=data.getvalue('s')

if service_data == "ss" :
     print ('<meta http-equiv="Refresh" content="0; url=http://localhost/saas.html">')

elif service_data == "sts" :
     print ('<meta http-equiv="Refresh" content="0; url=http://localhost/staas.html">')
elif service_data == "ps" :
     print ('<meta http-equiv="Refresh" content="0; url=http://localhost/paas.html">')

elif service_data == "is" :
     print ('<meta http-equiv="Refresh" content="0; url=http://localhost/iaas.html">')

else :
     print ('<meta http-equiv="Refresh" content="0; url=http://localhost/services.html">')


