##################### Extra Hard Starting Project ######################
import pandas as pd
import smtplib as smt
from datetime import datetime
from email_desc import *
import random

def send_mail(message, to_address):
    with smt.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_pass)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg= message
        )
        print("Mail sent")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

data = pd.read_csv("birthdays.csv")
curr_date = datetime.now().date()
# reciever = 0
reciever = data.loc[(data.month == curr_date.month) & (data.day == curr_date.day)]
# print(reciever)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
#
# for i in range(1, 4):
#     with open(file=f"letter_templates/letter_{i}.txt", mode="r") as file:
#         original_text = str(file.read())
#         original_text = original_text.replace("Angela", "Ankur")
#         print(original_text)
#
#     with open(file=f"letter_templates/letter_{i}.txt", mode="w") as file:
#         file.write(original_text)


if not reciever.empty:
    choice = random.randint(1, 3)
    with open(file = f"letter_templates\letter_{choice}.txt", mode="r") as file:
        message = str(file.read())
        message = message.replace("[NAME]", str(reciever.name.item()))
        # print(str(reciever.name.item()))
        # print(message)
        send_mail(f"subject:Happy Birthday\n\n{message}", str(reciever.email.item()))


# 4. Send the letter generated in step 3 to that person's email address.




