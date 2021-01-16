# my_email = "tanmaymutalikdesai@gmail.com"
# password = "Humpy100!"
# time_is_running = True
# now = dt.datetime.now()
# day = now.weekday()

# while time_is_running:
#     if day == 1:
#         with smtplib.SMTP("smtp.gmail.com") as connection:
#             connection.starttls()
#             connection.login(user=my_email, password=password)
#             connection.sendmail(from_addr=my_email,
#                                 to_addrs="mutalikdesaitanmay@gmail.com",
#                                 msg=f"Subject:Your Quote\n\n{lines}")
#             break
#     else:
#         print("Not the day")
#         pass
