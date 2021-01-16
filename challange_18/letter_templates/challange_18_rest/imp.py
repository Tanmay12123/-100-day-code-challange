import smtplib
import random
import datetime as dt

with open("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_18/quotes.txt",  errors='ignore') as data:
    lines = random.choice(data.readlines())
    print(lines)

my_email = "tanmaymutalikdesai@gmail.com"
password = "Humpy100!"

now = dt.datetime.now()
day = now.weekday()

if day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mutalikdesaitanmay@gmail.com",
                            msg=f"Subject:Your Quote From Python\n\n{lines}")


# date_of_birth = dt.datetime(year=2007, month=2, day=17)
