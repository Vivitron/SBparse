#!/usr/bin/python
# sbfunc.py

# tuple form is
# 0 = timestamp
# 1 = actor
# 2 = target
# 3 = damageamount
# 4 = resisttype
# 5 = pdtype
# 6 = spell
# 7 = killer
# 8 = killerguild
# 9 = dead
# 10 = deadguild
# 11 = effect
# 12 = tag
# 13 = healamount

import re
import sbparser

#tuple = timestamp, actor, target, damageamount, resisttype, pdtype, spell

def genericsort(data, actor, target, damageamount, resisttype, pdtype, spell):
    '''

    data is the list of tuples
    for other agruments:
    ''=ignore, 'y'=include in sort
    if another string, use value as filter for sort

    '''
    totaldmg = {}
    totalhealing = {}
    x = 0
    def uselines(string, arg):
        for datum in data:
            if re.search(str(string), datum[arg].lower()):
              ndata.append(datum)
    if actor and actor != 'y':
        ndata = []
        uselines(actor, 1)
        data = ndata
    if target and target != 'y':
        ndata = []
        uselines(target, 2)
        data = ndata
    if resisttype and resisttype != 'y':
        ndata = []
        uselines(resisttype, 4)
        data = ndata
    if pdtype and pdtype != 'y':
        ndata = []
        uselines(pdtype, 5)
        data = ndata
    if spell and spell != 'y':
        ndata = []
        uselines(spell, 6)
        data = ndata
    def filterkey(line):
        thekey = ''
        dealer = line[1]
        targ = line[2]
        rssttp = line[4]
        pdtp = line[5]
        spll = line[6]
        if actor == 'y':
            thekey += 'Dealer ' + line[1] + ','
        if target == 'y':
            thekey += ' Target ' + line[2] + ','
        if resisttype == 'y' and rssttp:
            thekey += ' Resist Type ' + line[4] + ','
        if pdtype == 'y' and pdtp:
            thekey += ' ' + line[5] + ','
        if spell == 'y' and spll:
            thekey += ' Spell ' + line[6] + ','
        return thekey
    for line in data:
        fkey = filterkey(line)
        dmg = line[3]
        healing = line[13]
        if fkey in totaldmg:
            totaldmg[fkey][0] += dmg
            totaldmg[fkey][1] += 1
            totaldmg[fkey][2] += healing
        else:
            totaldmg[fkey] = [dmg, 1, healing]
    def second(x):
        return x[1][0], x[1][2], x[1][1]
    return sorted(totaldmg.items(), key=second, reverse=True)

def pvpsort(data, actor, actguild, target, targuild):
    '''

    data is the list of tuples
    for other agruments:
    ''=ignore, 'y'=include in sort
    if another string, use value as filter for sort

    '''
    totalkills = {}
    pvpdata = []
    x = 0
    def uselines(string, arg):
        for datum in data:
            if re.search(str(string), datum[arg].lower()):
                pvpdata.append(datum)
    if actor and actor != 'y':
        uselines(actor, 7)
        x += 1
    if actguild and actguild != 'y':
        uselines(actguild, 8)
        x += 1
    if target and target != 'y':
        uselines(target, 9)
        x += 1
    if targuild and targuild != 'y':
        uselines(targuild, 10)
        x += 1
    if not x:
        pvpdata = data
    def filterkey(line):
        thekey = ''
        if actor == 'y':
            thekey += line[7]
        if actguild == 'y':
            thekey += 'of ' + line[8]
        if target == 'y':
            thekey += ' killed ' + line[9]
        if targuild == 'y':
            thekey += ' of ' + line[10]
        return thekey
    for line in pvpdata:
        if line[7]:
            fkey = filterkey(line)
            if fkey in totalkills:
                totalkills[fkey] += 1
            else:
                totalkills[fkey] = 1
    def second(x):
        return x[1]
    return sorted(totalkills.items(), key=second, reverse=True)



def testhardcall():
    allstuff = sbparser.make_list('logs/dmg.txt')
    data = allstuff[0]
    allparsed = genericsort(data, 'y', 'y', 'y', 'y', 'y', 'y')
    print(allparsed)


def main():
    print('This is a module dummy.')
    testhardcall()

#
# boiler plate
#
if __name__ == '__main__':
    main()
