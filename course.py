# Author: Chris Daw
# 11/18/17
# Course object for Classfinder schedule generator

class Course(object):
    def __init__(self, coursename='', title='', crn='', prof='', lecturetime='',
            labtime=''):
        self.coursename = coursename
        self.title = title
        self.crn = crn
        self.prof = prof
        self.lecturetime = lecturetime
        self.labtime = labtime

    def __getitem__(self, attr):
        return super(Course, self).__getattribute__(attr)

    def __setitem__(self, attr, value):
        self.__dict__[attr] = value

    def __str__(self):
        return ("Course: " + self.coursename + "\nName: " + self.title + \
                "\nCRN: " + self.crn + "\nProfessor: " + self.prof + \
                "\nClass Schedule: " + self.lecturetime + \
                "\nLab Schedule: " + self.labtime)
