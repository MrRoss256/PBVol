'''
Created on 15 Jul 2014

@author: Paul
'''

class ScheduleSDSFactory(object):
    '''
    classdocs
    '''


    def __init__(self, filename):
        '''
        Constructor

        Given an SDS file, constructs a set of schedules
        '''
        self.count = 0
        infile = open(filename, 'r')

        for line in infile:

            self.count += 1

            if line[0] == "1":
                print('one')

            if line[0] == "2":
                print('two')

            if line[0] == '3':
                print('three')

            if line[0] == '4':
                print('four')

            if line[0] == '5':
                print('five')


    def getSchedule(self):
        return self.count