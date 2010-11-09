#!/usr/bin/python
# webout.py

import os
import sys
sys.path.append(os.getcwd())
import sbparser
import sbfunc
import cgi
import re
from subprocess import call

header = 'Content-Type text/html\n\n'

formhtml = '''<HTML><HEAD><TITLE>
SBParsweb alpha 0.1
</TITLE></HEAD>
<FORM ACTION="/cgi-bin/webout.py">
<INPUT TYPE=hidden NAME=action VALUE=edit>
Log file is a relative path, one level up from server. Enter y in a field to 
sort by that field, or type any other string to filter that field by  the
string. Kill info is at the bottom.<P>
For example, try /logs/logname.txt for the file name and y for the actor. <p>
file:
<INPUT TYPE=text NAME=filename VALUE='' SIZE=50><P>
actor:
<INPUT TYPE=text NAME=actor VALUE='' >
target:
<INPUT TYPE=text NAME=target VALUE=''>
resist type:
<INPUT TYPE=text NAME=resisttype VALUE=''>
pd type:
<INPUT TYPE=text NAME=pdtype VALUE=''>
spell:
<INPUT TYPE=text NAME=spell VALUE=''><P>
<INPUT TYPE=submit></FORM></BODY></HTML><BR>'''

formhtml2 = '''<HTML><HEAD><TITLE>
SBParsweb alpha 0.1
</TITLE></HEAD>
<FORM ACTION="/cgi-bin/webout.py">
<INPUT TYPE=hidden NAME=action VALUE=edit>
Log file is a relative path, one level up from server. Enter y in a field to
sort by that field, or type any other string to filter that field by  the
string. Kill info after the line.<P>
file:
<INPUT TYPE=text NAME=filename VALUE=%s  SIZE=50><P>
actor:
<INPUT TYPE=text NAME=actor VALUE=%s>
target:
<INPUT TYPE=text NAME=target VALUE=%s>
resist type:
<INPUT TYPE=text NAME=resisttype VALUE=%s>
pd type:
<INPUT TYPE=text NAME=pdtype VALUE=%s>
spell:
<INPUT TYPE=text NAME=spell VALUE=%s><P>
<INPUT TYPE=submit></FORM></BODY></HTML><BR>'''

def main():
    form = cgi.FieldStorage()#creates a dict like object holding the html form values
    if form.has_key('action'):#action only exists after submit has been pressed
        runoptions(form)
    else:
        print header + formhtml

def runoptions(form):
    if 'filename' in form:
        filename = form['filename'].value
    else:
        filename = ''
    if 'actor' in form:
        actor = form['actor'].value.lower()
    else:
        actor = ''
    if 'target' in form:
        target = form['target'].value.lower()
    else:
        target = ''
    if 'resisttype' in form:
        resisttype = form['resisttype'].value.lower()
    else:
        resisttype = ''
    if 'pdtype' in form:
        pdtype = form['pdtype'].value.lower()
    else:
        pdtype = ''
    if 'spell' in form:
        spell = form['spell'].value.lower()
    else:
        spell = ''
    print header + formhtml2 % (filename, actor, target, resisttype, pdtype, spell)
    if filename[-3:] == "txt":
        if not os.path.isfile(os.path.abspath('../'+filename[:-3]+'csv')):
            call(["python","logtocsv.py",os.path.abspath('../'+filename)])
        filename = filename[:-3] + 'csv'
    data = []
    pvpdata = []
    thecsv = open(os.path.abspath('../'+filename))
    thecsv.readline() #burns the metadata line
    for line in thecsv:
        line = re.split(',',line[:-1])
        line[3] = int(line[3])
        line[13] = int(line[13])
        data.append(tuple(line))
    #prettyprint(sbfunc.genericsort(data, actor, target, '', resisttype, pdtype, spell))
    tableprettyprint(sbfunc.genericsort(data, actor, target, '', resisttype, pdtype, spell))
    print '<br> <hr> <br>'
    pvpprint(sbfunc.pvpsort(data, 'y', 'y', 'y', 'y'))

def prettyprint(dict):
    for i in dict:
        damage = i[1][0]
        healing = i[1][2]
        if damage > 0 and healing > 0:
            print i[0], ' For ', damage, 'dmg,', healing, 'healing over', i[1][1], 'hits, average hit =', damage/i[1][1], '<br>'
        elif damage > 0 and healing == 0:
            print i[0], ' For ', damage, 'damage over', i[1][1], 'hits, average hit =', damage/i[1][1], '<br>'
        elif damage == 0 and healing > 0:
            print i[0], ' For ', healing, 'healing over', i[1][1], 'hits, average hit =', healing/i[1][1], '<br>'
        else:
            print i[0], i[1][1], 'times', '<br>'

def tableprettyprint(dict):
    # Test to visually break up the data
    print '<table border="1">'
    for i in dict:
        damage = i[1][0]
        healing = i[1][2]
        if damage > 0 and healing > 0:
            print '<tr>', '<td>', i[0], ' For ', damage, 'dmg,', healing, 'healing over', i[1][1], 'hits, average hit =', damage/i[1][1], '</td>', '</tr>'
        elif damage > 0 and healing == 0:
            print '<tr>', '<td>', i[0], ' For ', damage, 'damage over', i[1][1], 'hits, average hit =', damage/i[1][1], '</td>', '</tr>'
        elif damage == 0 and healing > 0:
            print '<tr>', '<td>', i[0], ' For ', healing, 'healing over', i[1][1], 'hits, average hit =', healing/i[1][1], '</td>', '</tr>'
        else:
            print '<tr>', '<td>', i[0], i[1][1], 'times', '</td>', '</tr>'
    print '</table>'

def pvpprint(dict):
    for i in dict:
        print i[0], '<br>'


def wtf(data):
    '''wtf?'''
    print('<br><br>This is a test option.<br><br>')
    print data
    print '<br>End of test option<br>'

def purebyline(data):
    print('<br><br>This is a test option.<br><br>')
    for i in data:
        print i
    print '<br>End of test option<br>'

if __name__ == '__main__':
    main()
