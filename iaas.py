#!/usr/bin/python

import cgi,cgitb
import commands,thread,time,random
cgitb.enable()
print "Content-type:text/html"
print ""
x=str(5900+random.randrange(59100))
y=str(5900+random.randrange(59100))

data = cgi.FieldStorage()
os = data.getvalue('os')
ram = data.getvalue('ram')
cpu = data.getvalue('cpu')
hdd = data.getvalue('hdd')
def fn():
	if hdd=="live":
		cmd2="sudo websockify -D --web=/usr/share/novnc "+x+" 127.0.0.1:"+y
		cmd = "sudo virt-install --cdrom /root/Downloads/"+os+".iso --ram "+ram+" --vcpu "+cpu+" --nodisk --name my"+os+" --graphics vnc,listen=127.0.0.1,port="+y+",password=redhat"
		commands.getoutput(cmd2)
		commands.getoutput(cmd)
	else:
        	path="/var/lib/libvirt/images"
		cmd0="sudo qemu-img create -f qcow2 -b "+path+"/"+os+".qcow2 "+path+"/cl"+os+".qcow2"
		cmd1="sudo chmod o+rwx "+path+"/cl"+os+".qcow2"
		cmd2="sudo websockify -D --web=/usr/share/novnc "+x+" 127.0.0.1:"+y
		cmd = "sudo virt-install --name my"+os+" --ram "+ram+" --vcpu "+cpu+" --disk path="+path+"/cl"+os+".qcow2 --import --graphics vnc,listen=127.0.0.1,port="+y+",password=redhat"
		commands.getoutput(cmd0)
		commands.getoutput(cmd1)
		commands.getoutput(cmd2)
		commands.getoutput(cmd)

thread.start_new_thread(fn,())
time.sleep(10)

print "<body bgcolor=YellowGreen>"
print "<a href=http://127.0.0.1:"+x+">Click here to get your os:</a>"
print "</body>"

