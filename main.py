#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details. In this example I have used environmental variables.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain your list of birthdays.


import os
from datetime import datetime
import pandas
import random
import smtplib
# Get email address and password from environmental variables
MY_EMAIL = os.environ.get("MyEmail")
MY_PASSWORD = os.environ.get("Password")
# Today's date
today = datetime.now()
# Tuple with today's mondh and day
today_tuple = (today.month, today.day)
print(f"Today date (month, day) {today_tuple} \n")
print("Script successfully run.")
# Read birthday.csv file
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # Choose a random birthday letter
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # Update letter with the name of the person that has the birthday
        contents = contents.replace("[NAME]", birthday_person["name"])
    # Send letter via email to the email address found on the birthdays.csv
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
