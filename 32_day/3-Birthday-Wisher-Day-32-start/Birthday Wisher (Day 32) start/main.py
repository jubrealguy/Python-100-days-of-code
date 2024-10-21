# import smtplib

# my_email = "oladimeji12344321@gmail.com"
# password = "zpmhmouwarbqbhom"

# try:
#     # Use SMTP_SSL for port 465
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs="oladimeji12344321@yahoo.com", msg="Subject:Heelo Boy\n\nHello Jubreel, Thank you love")
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"Failed to send email: {e}")

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(year, month, day, day_of_week)

# date_of_birth = dt.datetime(year=1991, month=5, day=25, hour=3)
# print(date_of_birth)

with open('quotes.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        cleaned_line = line.replace('"', '')
        print(cleaned_line.strip())