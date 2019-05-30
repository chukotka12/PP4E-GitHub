#!/usr/bin/python
import cgi
import html

form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<title> Peply Page</title>')
if not 'user' in form:
    print('<h1>Who are you?</h1>')
else:
    print('<h1>Hello <i>%s</i>!</h1>' % html.escape(form['user'].value)) #cgi.escape