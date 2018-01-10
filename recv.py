#!/usr/bin/python

import cgi,MySQLdb,cgitb
cgitb.enable()
print "Content-type:text/html"
print ""

webdata=cgi.FieldStorage()

user=webdata.getvalue('u')
password=webdata.getvalue('p')


if user==None or password==None:
	print "<script>alert('Username or Password cannot be Empty!!!');</script>"
	print '<meta http-equiv="refresh" content="0;url=http://127.0.0.1/index.html">'
	
db = MySQLdb.connect("localhost","root","qawsedrftg","users_cloud")
cursor = db.cursor()

cursor.execute("select password from profile where username='"+user+"'")
data = cursor.fetchone()

if data==None:
		print "<body bgcolor=yellowgreen>"
		print "No such user!!"
		print "</body>"
else:
	if password==data[0]:
		print '<meta http-equiv="refresh" content="0;url=http://127.0.0.1/services.html">'
	else:
		print "<body bgcolor=yellowgreen>"
		print "Wrong password!!"
		print "</body>"

