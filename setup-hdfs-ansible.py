#!/usr/bin/python2

import commands as sp
import cgi

print("content-type: text/html")
print("")

fh = open('/var/www/cgi-bin/hosts', 'w')

form = cgi.FormContent()
master=[]
slave=[]
for i in form.keys():
	if 'm' in i:
		master.append(i)
	else:	
		slave.append(i)

fh.write("[master]" + "\n")	      
for i in master:
	if 'm' in i:
		fh.write(form[i][0] + "\n")
fh.write("[slave]" + "\n")
for i in slave:
	if 's' in i:
		fh.write(form[i][0] + "\n")
fh.close()

fvar = open('/var/www/cgi-bin/dir', 'w')
d=sp.getoutput("date")
fvar.write("master: m" + d[11:19] + "\n")
fvar.write("slave: s" + d[11:19] + "\n")
fvar.write("mip: " + form['mip1'][0] + "\n")
fvar.close()

sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/hadoop-nn.yml")
#sp.getoutput("ansible-playbook /project/hadoop-dn.yml")
sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/hadoop-dn.yml")
#sp.getoutput("sudo ansible-playbook  nm.yml -i hosts")
