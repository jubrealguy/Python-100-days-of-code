import smtplib
import datetime as dt
import pandas as pd
import random as rd

my_email = "oladimeji12344321@gmail.com"
password = "zpmhmouwarbqbhom"

now =  dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

friends = pd.read_csv('birthdays.csv')

birthday_dict = {(friend_row['month'], friend_row['day']): friend_row for (index, friend_row) in friends.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    print(birthday_person)
    file_path = f"letter_templates/letter_{rd.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person['name'])

    try:
        # Use SMTP_SSL for port 465
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=birthday_person['email'], 
                msg=f"Subject:Happy Birthday\n\n{content}"
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
