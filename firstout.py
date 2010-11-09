#!/usr/bin/python
# firstout.py

import sbparser
import sys
import sbfunc

ctr = 8

def prettyprint(dict):
    for i in dict:
        print i[0], '-->', i[1][0], 'dmg over', i[1][1], 'hits, avg dmg =', i[1][0]/i[1][1],

def main():
    '''Main control flow loop.

    Test options in the low 100's
    allstuff = [combat, pvpmessages, effects, leftovers]
    each of which is a list of tuples in it's own right.

    '''
    filename()
    test = sbparser.LogParse(logfilename)
    allstuff = test.make_list()
    data = allstuff[0]
    pvpdata = allstuff[1]
    effectdata = allstuff[2]
    notdata = allstuff[-1]
    while ctr != 0:
        start()
        if ctr == 1:
            prettyprint(sbfunc.genericsort(data, 'y', '', '', '', '', ''))
        elif ctr == 2:
            char = str(raw_input('Damage dealer:'))
            print char
            prettyprint(sbfunc.genericsort(data, char, 'y', '', 'y', '', 'y'))
        elif ctr == 3:
            prettyprint(sbfunc.genericsort(data, '', 'y', '', '', '', ''))
        elif ctr == 4:
            char = str(raw_input('spell:'))
            prettyprint(sbfunc.genericsort(data, 'y', '', '', '', '', char))
        elif ctr == 5:
            prettyprint(sbfunc.genericsort(data, '', 'y', 'y', 'y', '', 'y'))
        elif ctr == 6:
            print "Input: y or word to sort by, blank to ignore."
            actor = raw_input('actor:')
            target = raw_input('target:')
            resisttype = raw_input('resist type:')
            pdtype = raw_input('pdtype:')
            spell = raw_input('spell:')
            prettyprint(sbfunc.genericsort(data, actor, target, '', resisttype, pdtype, spell))
        elif ctr == 8:
            main()
        elif ctr == 100:
            print 'Raw dump of data from parse:'
            wtf(data)
        elif ctr == 101:
            print 'Line by line dump of data from parse:'
            purebyline(data)
        elif ctr == 102:
            test = ''
            print 'lines that were not parsed:'
            for i in notdata:
                test += i
            print test
        elif ctr == 103:
            for i in pvpdata:
                print i
        elif ctr == 104:
            for i in effectdata:
                print i
        elif ctr == 105:
            pvpac = {}
            for i in pvpdata:
                killer = i[1]
                if killer in pvpac:
                    pvpac[killer] += 1
                else:
                    pvpac[killer] = 1
            for i in pvpac.items():
                print i[0], "-->", i[1]
        elif ctr == 0:
            break
        else:
            print('\n\nPlease make a real choice!:\n\n')
    print('\n\nPlay to Crush.\n\n')

def filename():
    global logfilename
    if len(sys.argv) > 2:
        print('Usage: filename; or no arg')
        global ctr
        ctr = 0
    elif len(sys.argv) == 2:
        logfilename = sys.argv[1]
    else:
        logfilename = str(raw_input('Log file name:'))


def start():
    '''Main menue, and input for selection.'''
    print '\n\nFor log file:', logfilename
    print('Main options:')
    print('Top damage dealers: 1')
    print('Damage by name: 2')
    print('Top damage taken: 3')
    print('Damage by specific spell: 4')
    print('Damage by spell and resist: 5')
    print('Custom Sort: 6')
    print('New log file: 8')
    print('Exit: 0')
    global ctr
    ctr = int(input('\n\nMenue choice?:'))


def wtf(data):
    '''wtf?'''
    print('\n\nThis is a test option.\n\n')
    print data
    print '\nEnd of test option\n'

def purebyline(data):
    print('\n\nThis is a test option.\n\n')
    for i in data:
        print i
    print '\nEnd of test option\n'


#
# Boiler plate for exe
#

if __name__ == '__main__':
    main()
