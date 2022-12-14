import smtplib
import datetime as dt
import random
import pandas

my_email = "joestarjoseph025@gmail.com"
password = "###"     # use app password

now = dt.datetime.now()
day = now.day
month = now.month

data = pandas.read_csv("birthdays.csv")
b_day_dict = data.to_dict(orient="records")

for b_day in b_day_dict:
    random_letter = f"letter_{random.randint(1, 3)}.txt"
    to_email = b_day["email"]
    if b_day["month"] == month and b_day["day"] == day:
        name = b_day["name"]
        with open(file=f"letter_templates/{random_letter}", mode="r") as letter:
            content = letter.read()
            new_letter = content.replace("[NAME]", name)
            print(new_letter)
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg=f"Subject:HappyBirthDay, {name}\n\n{new_letter}")
