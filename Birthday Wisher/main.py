import smtplib
import datetime as dt
import random
import pandas as p

data = p.read_csv(r"Birthday Wisher\birthdays.csv").to_dict("records")

now = dt.datetime.now()
month = now.month
day = now.day

my_email = "YOUR_EMAIL"
password = "YOUR_EMAIL_PASSWORD"

for person in data:
    # Check if today matches a birthday in the birthdays.csv
    if person["month"]==month and person["day"]==day:
        # If true pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        filepath = fr"Birthday Wisher\letter_templates\letter_{random.randint(1,3)}.txt"
        with open(filepath,"r") as f:
            content = f.read()
            content = content.replace("[NAME]",person["name"])

        # with open("Birthday Wisher\quotes.txt") as f:
        #     quotesList = f.readlines()
        #     quote = random.choice(quotesList)

        # Send the letter generated in step 3 to that person's email address.
        receiver_mail = person["email"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=receiver_mail,
                msg=f"Subject:Happy Birthday!\n\n{content}"
            )