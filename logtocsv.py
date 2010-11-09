#!/usr/bin/python

import sbparser
import sys
#import sbfunc #unnecessary?

def main():
    '''
    create a .csv from the list of tuples
    returned by sbfunc.genericsort of the
    input file
    '''
    if len(sys.argv) == 2:
        logfilename = sys.argv[1]
    else:
        logfilename = str(raw_input('Log file name:'))

    csvfilename = logfilename[:-3] + 'csv'
    print("Creating " + csvfilename)
    print("This should take under 15 seconds.")
    csvfile = open(csvfilename, 'w')

    allstuff = sbparser.LogParse(logfilename).make_list()
    csvfile.write("ts,actor,target,damage,dtype,pd,spell,killer,killerguild,dead,deadguild,effect,tag,healamount")
#    for unit in allstuff[:-1]: #includes all except missedparse (damage,pvp,effect)
    for unit in allstuff[0:2]:    #includes just damage,pvp parse
        for row in unit:
            csvfile.write("\n")
            first = True
            for element in row:
                if not first:
                    csvfile.write(',')
                csvfile.write(str(element))
                first = False
    csvfile.write("\n")

if __name__ == '__main__':
    main()
