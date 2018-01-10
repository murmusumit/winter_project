#!/usr/bin/python

import cgi,cgitb
import commands
cgitb.enable()
print "Content-type:text/html"
print ""

webdata=cgi.FieldStorage()
name=webdata.getvalue('name')
size=webdata.getvalue('size')
type_storage=webdata.getvalue('type')
if type_storage=="object":
	commands.getoutput("sudo lvcreate --name "+name+" -V"+size+"G myvg/mypool --thin")
	commands.getoutput("sudo mkfs.xfs /dev/myvg/"+name)
	commands.getoutput("sudo mkdir /var/www/html/"+name)
	commands.getoutput("sudo mount /dev/myvg/"+name+" /var/www/html/"+name)
	commands.getoutput("sudo chmod 777 /var/www/html/"+name)

	f1 = open("/etc/exports","a")
	y = '/var/www/html/'+name+'  *(rw)\n'
	f1.write(y)
	f1.close()

	commands.getoutput("sudo exportfs -r")
	
	f2 = open("/var/www/html/"+name+"/"+name,"w")
	x = "#!/bin/bash\nsudo mkdir /mnt/"+name+"\nmount 127.0.0.1:/var/www/html/"+name+" /mnt/"+name
	f2.write(x)
	f2.close()
	commands.getoutput("sudo chmod +x /var/www/html/"+name+"/"+name)
	print "<body bgcolor=YellowGreen>"
	print "Please open url=127.0.0.1/"+name+" and download file named "+name+". Then run that file on terminal, your disk will be mounted in 		your system"
	print "</body>"
else:
	commands.getoutput("sudo lvcreate --name "+name+" -V"+size+"G myvg/mypool --thin")
	commands.getoutput("sudo mkdir /var/www/html/"+name)
	commands.getoutput("sudo chmod 777 /var/www/html/"+name)
	f1 = open("/etc/tgt/targets.conf","a")
	y = '<target '+name+'>\n'
	f1.write(y)
	y1 = 'backing-store /dev/myvg/'+name+'\n'
	f1.write(y1)
	y2 = '</target>\n'
	f1.write(y2)
	f1.close()
	commands.getoutput("sudo systemctl restart tgtd")
	f2 = open("/var/www/html/"+name+"/"+name+"_login","w")
	x = "#!/bin/bash\nsudo iscsiadm --mode discoverydb --type sendtargets --portal 127.0.0.1 --discover\nsudo iscsiadm --mode node --targetname 		"+name+" --portal 127.0.0.1:3260 --login"
	f2.write(x)
	f2.close()
	f3 = open("/var/www/html/"+name+"/"+name+"_logout","w")
	z = "#!/bin/bash\nsudo iscsiadm --mode node --targetname "+name+" --portal 127.0.0.1:3260 --logout"
	f3.write(z)
	f3.close()
	commands.getoutput("sudo chmod +x /var/www/html/"+name+"/"+name+"_login")
	commands.getoutput("sudo chmod +x /var/www/html/"+name+"/"+name+"_logout")
	print "<body bgcolor=YellowGreen>"
	print "Please open url=127.0.0.1/"+name+" and download file named "+name+"_login and "+name+"_logout for logging in and logging out 		respectively"
	print "</body>"
