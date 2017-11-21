from course import Course
from postreq import PostReq

import re
import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://admin.wwu.edu/pls/wwis/wwsktime.ListClass'
    re_schedule = re.compile("[MTWRF]{1,5}\s+[0-1][0-9]:[0-5][0-9]-[0-1][0-9]:[0-5][0-9]\s+(am|pm)")

    postreq1 = PostReq("CSCI", "145")

    form_data = postreq1.form_data

    request = requests.post(url, data=form_data)
    soup = BeautifulSoup(request.content, 'html.parser')
    soup.prettify()

    courses = []

    tempcourse = Course()
    firstthree = 0 #we know what the first three elements are
    cells = soup.find_all("td")
    for cell in cells:
        for contents in cell:
            newsection = postreq1.subject + " " + postreq1.coursenum
            if contents.name == "font":
                if contents.text == newsection:
                    if tempcourse.coursename != '':
                        courses.append(tempcourse)
                    firstthree = 0
                    tempcourse = Course()
                    tempcourse.coursenum = contents.text
                if firstthree < 3:
                    set_next_element(tempcourse, contents.text)
                    firstthree += 1
                if re.match(re_schedule, contents.text.lstrip()):
                    set_next_element(tempcourse, contents.text)
            if contents.name == "input":
                tempcourse.crn = contents.get('value')
    courses.append(tempcourse)

    for item in courses:
        print(item)
        print()

def set_next_element(course, value):
        elements = ['coursename', 'title', 'crn', 'prof', 'lecturetime', 'labtime']
        for element in elements:
            if course[element] == '':
                course[element] = value
                break

if __name__ == '__main__':
    main()
