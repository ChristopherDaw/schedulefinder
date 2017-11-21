# Author: Chris Daw
# 11/18/17
# Post request object for Classfinder schedule generator
# User input subject goes to form_data[2][1]
# User input course number goes to form_data[5][1]

class PostReq:
    def __init__(self, subject, coursenum):
        self.subject = subject
        self.coursenum = coursenum
        self.form_data = form_data = (
                ('sel_subj', 'dummy'), ('sel_subj', 'dummy'),('sel_subj', subject),
                ('term', '201810'), ('sel_inst', 'ANY'), ('sel_crse', coursenum),
                ('sel_gur', 'dummy'), ('sel_gur', 'dummy'), ('sel_gur', 'All'),
                ('sel_day', 'dummy'), ('sel_open', 'dummy'), ('sel_crn', ''),
                ('begin_hh', '0'), ('begin_mi', 'A'), ('end_hh', '0'),
                ('end_mi', 'A'), ('sel_cdts', '%'))
