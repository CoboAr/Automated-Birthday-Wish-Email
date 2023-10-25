# Automated-Birthday-Wish-Email

## Requirements
pip install pandas

## What is Automated-Birthday-Wish-Email?
It is an automated software that sends a birthday wish letter to user's contacts implemented with pandas python library, and os, random, datetime, smtplib python modules.  

## How does it work?
In order to send emails with python code, the email service provider needs to be configured first. I have used Gmail, and I have done the configuration for Gmail email service, however all email free service providers work the same way if their email configuration is done accordingly.  

### Gmail configuration  
Step 1:  Make sure you've got the correct smtp address for your email provider: smtp.gmail.com   
Step 2: Go to https://myaccount.google.com/  
Select Security on the left and scroll down to How you sign in to Google. Enable 2-Step Verification.     
Step 3: Click on 2-Step Verification again, and scroll to the bottom.   
<ul>
  <li>There you can add an App password.</li>
  <li>Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.</li>    
  <li>COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.</li>
  <li>Use this App password in your Python code instead of your normal password.</li>
</ul>     

Step 4: Add a port number by changing your code to this:       
smtplib.SMTP("smtp.gmail.com", port=587)


Once the Gmail configuration is completed and main.py is run, the program will check today's date(month, day) with the date(month,day) on birthdays.csv where birthdays.csv should be populated by user with his contacts information in this format 'name,email,year,month,day'.  

<img width="1024" alt="Screenshot 2023-10-24 at 5 05 34 PM" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/11606c51-23ab-4ed5-96bc-fb690483d519">

If today's date matches with the birthday of any of the contacts found in birthdays.csv, then the program chooses randomly one out of three birthday wish letters found in the letter_templates.   

<img width="365" alt="Screenshot 2023-10-24 at 5 07 22 PM" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/c6bd6fdc-8fd7-4e38-b7d3-3a2bb7f67184">

It updates [NAME] with the contact's name for birthdays.csv and it sends the letter as an email to the email address found in birthdays.csv.  

<img width="403" alt="Screenshot 2023-10-24 at 5 12 29 PM" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/dd7984fe-d984-4cea-8f83-804bf42b7e74">

Finally, the birthday wish email is received on the email address provided in birthdays.csv.     

<img width="1045" alt="Email_Birthday_Wish_Received" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/bf74a33f-1d4c-40a0-b18c-cdda6ee3dd95">

## Automation

In order to run the script on a daily basis automatically, I have used PythonAnywhere which is is an online integrated development environment and web hosting service based on the Python programming language. 

Step1: Create/Sign in in PythonAnywhere   

<img width="688" alt="PythonAnywhere_ login_page" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/61699e40-aad8-47da-a983-935d2407c097">

Step 2: Click Files

<img width="820" alt="Click Files" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/329c0449-7cdb-4843-84a4-59944fa05368">

Step 3: Upload main.py and birthdays.csv as files   

<img width="1440" alt="Upload main py and  birthdays scv" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/34d9ff98-4aba-4b6b-94e5-cec8b7933b0b">

Step 4: Create a new directory named letter_templates and upload inside this directory 3 letters: letter1.txt, letter2.txt, letter3.txt   

<img width="1440" alt="letter_templates_directory" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/42c69857-cdbe-4332-8c2a-e54214adb75c">   

<img width="1440" alt="project uploaded in PythonAnywhere" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/be1ad10f-a17c-483b-961a-85ca6fe2b2aa">    

Step 5: Click main.py and then Bash console here  

<img width="820" alt="Click main py file" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/7ea5505c-5b90-4fa7-8ad6-0c5a75b6abc5">

<img width="816" alt="Click Bash Console Here" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/658eae7f-a033-45c1-b773-26fe594e1c9f">  

Step 6: Add environmental variables for email and password  (The asterixs should be replaced by the app password generated during Gmail configuration Step 3.

<img width="1430" alt="Add Environmental Variables" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/36cb65cc-2bdc-4e9c-9ce9-4d495b27bfbc">    

Step 7: Run scrip with command "python3 main.py"   

<img width="1424" alt="Run Script" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/95340d49-107e-477a-901b-ab23de7808d3">   


Step 8: Click Tasks and setup a daily task for 1 month

<img width="816" alt="Click Tasks" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/c29f9bd3-0b1f-4921-b36f-69853b097b13">      


After setting the time when we want to run the script on a daily basis, we need to add the run command including the environmental variables otherwise the script won't run:

export MyEmail=emripacaktuar@gmail.com; export  Password=****************; python3 main.py

Then click create button and the script is set to run on the specified time, on daily basis for 1 month. Each month the task needs to be recreated in order to run the script automatically all year round.     

<img width="1438" alt="Create Task" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/631939bf-d58e-461f-a6a0-ea4f4d65bc50">

<img width="1439" alt="Create Task" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/05e5708f-5e9e-43b6-92f2-3ae3b3b49577">

<img width="1440" alt="Task Created" src="https://github.com/CoboAr/Automated-Birthday-Wish-Email/assets/144629565/c39ebb17-5cc0-431b-bb6d-a141a27b2f45">

Enjoy! And please do let me know if you have any comments, constructive criticism, and/or bug reports.
## Author
## Arnold Cobo





