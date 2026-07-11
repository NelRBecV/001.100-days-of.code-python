##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime
import os
from dotenv import load_dotenv()
from random import randint

load_dotenv()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv - DONE
def create_letter(guest: str) -> str:
    letter_body: list = []    
    for letter in range(1,4):
        with open(f"letter_templates\letter_{letter}.txt", "r") as inv_letter:
            letter_body.append(inv_letter.read())
    invitation: str = str(letter_body[randint(0,2)]).replace("[NAME]", guest)
    return invitation

# 1. Update the birthdays.csv - DONE
data = pandas.read_csv("birthdays.csv").to_dict(orient="records")
date = datetime.datetime
c_month: int = date.now().month
c_day: int = date.now().day

# 2. Check if today matches a birthday in the birthdays.csv - DONE
for person in data:    
    if not person['month'] == c_month and not person['day'] == c_day:
        continue
        
    full_name: list = person['name'].split()
    email: str = person['email']
    name: str = full_name[0]
    letter: str = create_letter(name)

    user: str = os.getenv("USER_MAIL")
    passw: str = os.getenv("PSWD_MAIL")
    message: str = f"From:{user}\nTo:{email}\nSubject: Happy Birthday!!!\n\n{letter}"

    # 4. Send the letter generated in step 3 to that person's email address. - DONE
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as email_congrats:
        email_congrats.starttls()
        email_congrats.login(user=user, password=passw)
        email_congrats.sendmail(from_addr=user, to_addrs=email, msg=message)
