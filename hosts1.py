#!/usr/bin/python2

print("content-type: text/html")
print("")

import cgi
import commands  as sp


form = cgi.FormContent()
#print(form)
p=open('/var/www/cgi-bin/hosts1','w')
for i in form.keys():
	if 'j' in i:
		if '1' in i:
			p.write("[jobtracker]\n")
		else:
			pass	
		p.write(form[i][0] + "\n")
	elif 't' in i:
		if '1' in i:
			p.write("[tasktracker]\n")
		else:
			pass
		p.write(form[i][0] + "\n")
p.close()

p1=open('/var/www/cgi-bin/ip1.yml','w')
for i in form.keys():
	if 'j' in i:
		p1.write("jip: " + form[i][0])
p1.close()

sp.getoutput("sudo ansible-playbook /var/www/cgi-bin/mapred.yml")



