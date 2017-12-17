#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
os = data.getvalue('os')
ram = data.getvalue('ram')
cpu = data.getvalue('cpu')
hdd = data.getvalue('hdd')

if hdd=="live":
	cmd = "sudo virt-install --cdrom /var/www/html/iso/"+os+".iso --ram "+ram+" --vcpu "+cpu+" --nodisk --name my"+os+" --graphics vnc,listen=127.0.0.1,port=5912,password=redhat"
else:
	cmd = "sudo virt-install --cdrom /var/www/html/iso/"+os+".iso --ram "+ram+" --vcpu "+cpu+" --disk "+hdd+" --name my"+os+" --graphics vnc,listen=127.0.0.1,port=5912,password=redhat"

output=commands.getoutput(cmd)

print cmd
print output
