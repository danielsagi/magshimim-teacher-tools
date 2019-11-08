# magshimim-teacher-tools
A collection of tools for Magshimim teachers

## Tools:
### auto_download.py
This tool is for downloading students submitted files automatically,  

#### Steps to configure:
1. Change the raw_cookies variable to your cookie.
    This cookie can be acquired while requesting the site, by looking at the `Network` session in Google Chrome, filtering only to  DOC, and looking at the HTTP request with the cookie starts with 'lmssessionkey2'. Copy the `lmssessionkey2=...;` (until the semicolon)
2. Acquire your class id:  
    This is achieved by clicking on your class in EDU,  
    looking at url:
    https://magshimim.edu20.org/teacher_lessons/list/<class_id>
3. Acquire your task id:  s
    This is achieved by clicking on your desired assignment in the assignments tabs in EDU,  
    looking at url:
    https://magshimim.edu20.org/teacher_freeform_assignment/show/<task_id>
4. Run the script with the ids as parameters.

The script will scrape all of your students files automatically, and for each student, create a folder named with his name, containing his submitted files.

The folders will be created next to the script's executed path