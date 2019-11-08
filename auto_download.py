#!/usr/bin/env python
# -------------------------
# Written by: Daniel Sagi
# -------------------------
import os
import sys
import requests
from bs4 import BeautifulSoup

s = requests.Session()

raw_cookies = "" # change to content of Cookies from http requests
s.headers.update({"Cookie": raw_cookies})

if len(sys.argv) < 3:
    print("Usage: ./auto_download.py <class_id> <task_id>")
    sys.exit(1)

BASE_URL = "http://ilearn.cyber.org.il/"
CLASS_ID = sys.argv[1] # example: "1138084"
TASK_ID = sys.argv[2] # example: "8796494"


def download_students_files(students, task_id):
    for student_id, student_name in students.items():
        print("[+] Downloading files for {}".format(student_name))
        full_url = BASE_URL + "/teacher_freeform_assignment/grade/{}?offset=0&student={}".format(task_id, student_id)
        soup = BeautifulSoup(s.get(full_url).text, features="html.parser")

        for a in soup.find_all('a', href=True):
            if "/files/" in a['href']:
                f_name = '/' + a['href'].split('/')[3]
                with open(student_name + f_name, 'wb') as f: 
                    f.write(s.get(BASE_URL + a['href']).content)


def get_student_list(class_id):
    full_url = BASE_URL + "/teacher_students/list/{}".format(class_id)
    soup = BeautifulSoup(s.get(full_url).text, features="html.parser")
    
    students = dict()
    for a in soup.find_all('a', href=True):
        if '/user/show/' in a['href'] and not a.find('img'):
            student_name = a.text.replace(', ', '_')
            student_id = a['href'].split('/')[3]
            students[student_id] = student_name
    return students


def create_student_folders(student_names):
    for name in student_names:
        try:
            os.mkdir(name)
        except FileExistsError:
            pass


def main():
    students = get_student_list(CLASS_ID)
    create_student_folders(students.values())

    # downloading files of students to their corresponding folder
    download_students_files(students, TASK_ID)

if __name__ == '__main__':
    main()