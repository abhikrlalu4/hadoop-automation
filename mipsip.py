#!/usr/bin/python2

print("content-type: text/html")
print("")

import cgi
import commands as sp

form=cgi.FieldStorage()
jt = form.getvalue("jt")
tt = form.getvalue("tt")
#print("form.keys()")



print("""<form action="hosts1.py">""")
j = 1
while j <= int(jt):
	print("JT {0} : <input name='jip{0}' /><br />".format(j))
	j+=1

j = 1
while j <= int(tt):
	print("TT {0} : <input name='tip{0}' /><br />".format(j))
	j+=1

print("""<input type='submit'>
</form>""")
