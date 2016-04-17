import datetime
import csv


class timetable(object):

    def __init__(self, d, l, loc1='FPH', loc2='Hughesdale'):
        self.d = d
        self.l = l
        self.loc1 = loc1
        self.loc2 = loc2

    def event(self, type):
        d = self.d
        l = self.l
        dta = 0
        if type == 'yy':
            dta = 3 - d.weekday()
        elif type == 'vd':
            dta = 1 - d.weekday()
        if dta <= 0:
            dta += 7
        dit = d+datetime.timedelta(dta)
        dfa = 4 - d.weekday()
        if dfa <= 0:
            dfa += 7
        dif = d + datetime.timedelta(dfa)
        dsa = 6 - d.weekday()
        if dsa <= 0:
            dsa += 7
        dis = d + datetime.timedelta(dsa)
        writer = csv.writer(open(type+'.csv', 'w'))
        for t in range(l):
            if type == 'yy':
                writer.writerow(['Thursday, ' +
                                 str(dit+datetime.timedelta(7*t)) +
                                ', 6.30pm' + ', 8pm' + ', Hughesdale'])
                writer.writerow(['Sunday, ' + str(dis+datetime.timedelta(7*t)) +
                                ', 6pm' + ', 7.30pm'+', FPH'])
            elif type == 'vd':
                writer.writerow(['Tuesday, ' +
                                 str(dit+datetime.timedelta(7*t)) +
                                ', 6.30pm' + ', 8.30pm' + ', FPH'])
                writer.writerow(['Friday, ' + str(dif+datetime.timedelta(7*t)) +
                                ', 6.30pm' + ', 8.30pm' + ', Hughesdale'])
                writer.writerow(['Sunday, ' + str(dis+datetime.timedelta(7*t)) +
                                ', 2pm' + ', 4pm' + ', FPH'])

            elif type == 'tjd':

                writer.writerow(['Sunday, ' + str(dis+datetime.timedelta(7*t)) +
                                ', 4pm' + ', 6pm' + ', FPH'])

            elif type == 'sms':

                if t <= l/4:

                    writer.writerow(['Sunday, ' +
                                     str(dis+datetime.timedelta(28*t)) +
                                    ', 10am' + ', 12.30pm' + ', FPH'])

    def together(self):
        self.event('yy')
        self.event('vd')
        self.event('tjd')
        self.event('sms')

test = timetable(datetime.date(2015, 11, 25), 6)

test.together()
