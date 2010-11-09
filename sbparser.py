#/usr/bin/python
# sbparser.py

import sys
import re

class DmgParse:
    def passivedef(self):
        '''

        (2:59:01) Insan blocks Vivitron's attack.
        (timestamp, actor, target, damageamount, resisttype, pdtype, spell)

        '''
        info = re.findall(
    r'\((.*?)\)\s(\w+)\s.*?(blocks|dodges|parries)\s(\w+)\s?.*?\'s\sattack'
        , self.line)
        for i in info:
            timestamp, target, pdtype, actor = i
            spell = ''
            resisttype = ''
            damageamount = 0
            killer = ''
            killerguild = ''
            dead = ''
            deadguild = ''
            effect = ''
            tag = ''
            healamount = 0
            tpl = timestamp, actor, target, damageamount, resisttype, pdtype, spell, killer, killerguild, dead, deadguild, effect, tag, healamount
            self.listoftuples.append(tpl)
            return True

    def misses(self):
        '''

        (2:58:54) Insan misses Vivitron.
        (timestamp, actor, target, damageamount, resisttype, pdtype, spell)

        '''
        info = re.findall(
    r'\((.*?)\)\s(\w+)\s.*?(misses)\s(\w+).*'
        , self.line)
        for i in info:
            timestamp, actor, pdtype, target = i
            spell = ''
            resisttype = ''
            damageamount = 0
            killer = ''
            killerguild = ''
            dead = ''
            deadguild = ''
            effect = ''
            tag = ''
            healamount = 0
            tpl = timestamp, actor, target, damageamount, resisttype, pdtype, spell, killer, killerguild, dead, deadguild, effect, tag, healamount
            self.listoftuples.append(tpl)
            return True

    def physdmg(self):
        '''

        (2:58:57) Vivitron hits Insan for 13 points of damage.
        (timestamp, actor, target, damageamount, resisttype, pdtype, spell)

        '''
        info = re.findall(
    r'\((.*?)\)\s(\w+)\s.*?hits\s(\w+)\s.*?for\s(\d+)\spoints?\sof\sdamage'
        , self.line)
        for i in info:
            timestamp, actor, target, damageamount = i
            damageamount = int(damageamount)
            spell = ''
            resisttype = 'physical'
            pdtype = ''
            killer = ''
            killerguild = ''
            dead = ''
            deadguild = ''
            effect = ''
            tag = ''
            healamount = 0
            tpl = timestamp, actor, target, damageamount, resisttype, pdtype, spell, killer, killerguild, dead, deadguild, effect, tag, healamount
            self.listoftuples.append(tpl)
            return True

    def spelldmg(self):
        '''

        (2:58:32) Vivitron's Hedge of Thorns impales Insan for 43 points of damage!
        (timestamp, actor, target, damageamount, resisttype, pdtype, spell)

        '''
        info = re.findall(
    r'\((.*?)\)\s(\w+?)\'s\s(.+)\s(\w+)\s(\w+)\sfor\s(\d+)\spoints?\sof\sdamage'
        , self.line)
        for i in info:
            timestamp, actor, spell, resisttype, target, damageamount = i
            damageamount = int(damageamount)
            pdtype = ''
            killer = ''
            killerguild = ''
            dead = ''
            deadguild = ''
            effect = ''
            tag = ''
            healamount = 0
            tpl = timestamp, actor, target, damageamount, resisttype, pdtype, spell, killer, killerguild, dead, deadguild, effect, tag, healamount
            self.listoftuples.append(tpl)
            return True

    def dotdmg(self):
        """

        (7:37:05) Insan sufferes 143 points of damage from Vivitron's poison!
        (timestamp, actor, target, damageamount, resisttype, pdtype, spell)

        """
        info = re.findall(
    r'\((.*?)\)\s(\w+?)\s\w+\s(\d+)\spoints?\sof\sdamage\sfrom\s(\w+?)\'s\s(\w+)'
        , self.line)
        for i in info:
            timestamp, target, damageamount, actor, resisttype = i
            damageamount = int(damageamount)
            pdtype = ''
            spell = ''
            global listoftuples
            killer = ''
            killerguild = ''
            dead = ''
            deadguild = ''
            effect = ''
            tag = ''
            healamount = 0
            tpl = timestamp, actor, target, damageamount, resisttype, pdtype, spell, killer, killerguild, dead, deadguild, effect, tag, healamount
            self.listoftuples.append(tpl)
            return True

    def heals(self):
        '''
        CURRENTLY NOT RECORDED IN THE PARSE
        (7:24:08) Vivitron's Prayer of Recovery heals Insan for 242 points.
        (timestamp, actor, target, damageamount, resisttype, pdtype, spell)

        '''
        info = re.findall(
    r'\((.*?)\)\s(\w+?)\'s\s(.+)\s(heals)\s(\w+)\sfor\s(\d+)\spoints?'
        , self.line)
        for i in info:
            timestamp, actor, spell, resisttype, target, damageamount = i
            healamount = int(damageamount)
            damageamount = 0
            pdtype = ''
            killer = ''
            killerguild = ''
            dead = ''
            deadguild = ''
            effect = ''
            tag = ''
            tpl = timestamp, actor, target, damageamount, resisttype, pdtype, spell, killer, killerguild, dead, deadguild, effect, tag, healamount
            self.listoftuples.append(tpl)
            return True

class PvpParse:
    def pvpspam(self):
        """

        (7:42:37) [PvP] Insan of Decisive was killed by Vivitron of Decisive!
        (7:42:44) [PvP] Vivitron of Decisive was killed by Insan of Decisive!

        """
        info = re.findall(
    r'\((.*?)\)\s.PvP.\s(\w+)\sof\s(.*?)\swas\skilled\sby\s(\w+)\sof\s(.*?)!'
        , self.line)
        info2 = re.findall(
    r'\((.*?)\)\s.PvP.\s(\w+)\sof\s(.*?)\swas\skilled\sby\s(\w+).*?!'
        , self.line)
        info3 = re.findall(
    r'\((.*?)\)\s.PvP.\s(\w+).*?was\skilled\sby\s(\w+).*?!'
        , self.line)
        for i in info:
            timestamp, dead, deadguild, killer, killerguild = i
            tpl = timestamp, '', '', 0, '', '', '', killer, killerguild, dead, deadguild, '', '', 0
            self.pvpinfo.append(tpl)
            return True
        for i in info2:
            timestamp, dead, deadguild, killer, = i
            killerguild = ''
            tpl = timestamp, '', '', 0, '', '', '', killer, killerguild, dead, deadguild, '', '', 0
            self.pvpinfo.append(tpl)
            return True
        for i in info3:
            timestamp, dead, killer = i
            killerguild = ''
            deadguild = ''
            tpl = timestamp, '', '', 0, '', '', '', killer, killerguild, dead, deadguild, '', '', 0
            self.pvpinfo.append(tpl)
            return True

class EffectParse:
    def powers(self):
        info = re.findall(
    r'\((.*?)\)\s(\w+)\scan\sno\slonger\suse\spowers!'
        , self.line)
        info2 = re.findall(
    r'\((.*?)\)\s(\w+)\'s\spower\sabilities\sreturn.'
        , self.line)
        info3 = re.findall(
    r'\((.*?)\)\s(\w+)\'s\spowerblock\simmunity\shas\sworn\soff.'
        , self.line)
        for i in info:
            timestamp, target = i
            effect = 'powers'
            tag = 'on'
            tpl = timestamp, '', target, 0, '', '', '', '', '', '', '', effect, tag, 0
            self.effectdata.append(tpl)
            return True
        for i in info2:
            timestamp, target = i
            effect = 'powers'
            tag = 'off'
            tpl = timestamp, '', target, 0, '', '', '', '', '', '', '', effect, tag, 0
            self.effectdata.append(tpl)
            return True
        for i in info3:
            timestamp, target = i
            effect = 'powers'
            tag = 'immuneoff'
            tpl = timestamp, '', target, 0, '', '', '', '', '', '', '', effect, tag, 0
            self.effectdata.append(tpl)
            return True

    def stuns(self):
        info = re.findall(
    r'\((.*?)\)\s(\w+)\sis\sstunned!'
        , self.line)
        info2 = re.findall(
    r'\((.*?)\)\s(\w+)\sis\sno\slonger\sstunned.'
        , self.line)
        info3 = re.findall(
    r'\((.*?)\)\s(\w+)\'?s?\sstun\simmunity\shas\sworn\soff.'
        , self.line)
        for i in info:
            timestamp, target = i
            effect = 'stun'
            tag = 'on'
            tpl = timestamp, '', target, 0, '', '', '', '', '', '', '', effect, tag, 0
            self.effectdata.append(tpl)
            return True
        for i in info2:
            timestamp, target = i
            effect = 'stun'
            tag = 'off'
            tpl = timestamp, '', target, 0, '', '', '', '', '', '', '', effect, tag, 0
            self.effectdata.append(tpl)
            return True
        for i in info3:
            timestamp, target = i
            effect = 'stun'
            tag = 'immuneoff'
            tpl = timestamp, '', target, 0, '', '', '', '', '', '', '', effect, tag, 0
            self.effectdata.append(tpl)
            return True

    def movespeed(self):
        """parse for root and snare

        does not do snare off tags yet.

        """
        info = re.findall(
    r'\((.*?)\)\s(\w+)\s.+?immobilized!'
        , self.line)
        info2 = re.findall(
    r'\((.*?)\)\s(\w+)\s.+?immobilized.'
        , self.line)
        info3 = re.findall(
    r'\((.*?)\)\s(\w+)\sbegins\sto\sstumble.'
        , self.line)
        for i in info:
            timestamp, target = i
            effect = 'root'
            tag = 'on'
            tpl = timestamp, '', target, 0, '', '', '', '', '', '', '', effect, tag, 0
            self.effectdata.append(tpl)
            return True
        for i in info2:
            timestamp, target = i
            effect = 'root'
            tag = 'off'
            tpl = timestamp, '', target, 0, '', '', '', '', '', '', '', effect, tag, 0
            self.effectdata.append(tpl)
            return True
        for i in info3:
            timestamp, target = i
            effect = 'snare'
            tag = 'on'
            tpl = timestamp, '', target, 0, '', '', '', '', '', '', '', effect, tag, 0
            self.effectdata.append(tpl)
            return True

class MissedParse:

    def missedline(self):
        self.exceptions.append(self.line)


class LogParse(DmgParse, EffectParse, PvpParse, MissedParse):
    ''' Class to parse logfile, pass in logfile name.

    '''

    def __init__(self, logfile):
        LogParse.logfile = logfile

    def make_list(self):
        '''

        translate each line into a tuple, and make a string of the tuples
        tuple = timestamp, actor, target, damageamount, resisttype, pdtype, spell

        '''
        lf = open(LogParse.logfile)
        self.lines = lf.readlines()
        self.listoftuples = [] #one tuple per parsed line
        self.exceptions = []
        self.pvpinfo = []
        self.effectdata = []
        for line in self.lines:
            self.line = line
            if DmgParse.spelldmg(self):
                pass
            elif DmgParse.physdmg(self):
                pass
            elif DmgParse.passivedef(self):
                pass
            elif DmgParse.misses(self):
                pass
            elif DmgParse.dotdmg(self):
                pass
            elif PvpParse.pvpspam(self):
                pass
            elif DmgParse.heals(self):
                pass
            elif EffectParse.powers(self):
                pass
            elif EffectParse.stuns(self):
                pass
            elif EffectParse.movespeed(self):
                pass
            else:
                MissedParse.missedline(self)
        # Add new information types BEFORE exceptions.
        return self.listoftuples, self.pvpinfo, self.effectdata, self.exceptions


#
# Debuging code only below:
#
def main():
    """Simple debuging

    The prefered way to do this is run firstout.py and use option 9.

    """
    args = sys.argv[1:]
    if not args:
        print("usage [filename]")
        sys.exit(1)
    for element in make_list(args[0]):
        print(element)

#
# Boiler plate for execution
#

if __name__ == '__main__':
    main()
