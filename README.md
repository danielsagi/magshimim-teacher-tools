# magshimim-teacher-tools
A collection of tools for Magshimim teachers

## Tools:
### auto_download.py
This tool is for downloading students submitted files automatically,  

#### Steps to configure:
1. change the raw_cookies variable to your cookie.
2. acquire your class id:  
    this is achieved by clicking on your class in EDU,  
    looking at url:
    https://magshimim.edu20.org/teacher_lessons/list/<class_id>
3. acquire your task id:  s
    this is achieved by clicking on your desired assignment in the assignments tabs in EDU,  
    looking at url:
    https://magshimim.edu20.org/teacher_freeform_assignment/show/<task_id>
4. run the script with the ids as parameters.

The script will scrape all of your students files automatically, and for each student, create a folder named with his name, containing his submitted files.

The folders will be created next to the script's executed path