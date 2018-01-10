#!/usr/bin/python

import cgi
import cgitb
import commands,random
cgitb.enable()
print "Content-type:text/html"
print ""

x=str(random.random())
x=x[-4:]
print x
data=cgi.FieldStorage()

val=data.getvalue('s')
if val == "python":
	commands.getoutput("sudo docker run -itd -p "+x+":4200 python  bash")
	print ('<meta http-equiv="refresh" content="5; url=http://127.0.0.1:'+x+'">')
	print "Please enter <br>Username=python<br>Password=123"
elif val == "linux":
	commands.getoutput("sudo docker run -itd -p "+x+":4200 linux  bash")
	print ('<meta http-equiv="refresh" content="5; url=http://127.0.0.1:'+x+'">')
	print "Please enter <br>Username=linux<br>Password=123"
