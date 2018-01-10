#!/usr/bin/python

import cgi
import MySQLdb
import cgitb

cgitb.enable()
print "Content-type:text/html"
print ""

webdata = cgi.FieldStorage()
fname = webdata.getvalue('fname')
lname = webdata.getvalue('lname')
user = webdata.getvalue('user')
pass1 = webdata.getvalue('pass1')
pass2 = webdata.getvalue('pass2')
email = webdata.getvalue('email')

if fname==None or lname==None or user==None or pass1==None or pass2==None or email==None:
	print "Please Fill All the fields"
	exit()
if pass1!=pass2:
	print "hii"
	print "Password doesn't match!"
	exit()

db = MySQLdb.connect("localhost","root","qawsedrftg","users_cloud")

cursor = db.cursor()

cursor.execute("select * from profile where username='"+user+"'")

data = cursor.fetchone()

if data==None:
	add = "insert into profile values('','"+fname+"','"+lname+"','"+user+"','"+pass1+"','"+email+"')"
	cursor.execute(add)
	db.commit()
	print "Registration Successful"
else:
	print "Username Taken"
