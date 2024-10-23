import smtplib
import datetime as dt
import random as rd

my_email = "oladimeji12344321@gmail.com"
password = "zpmhmouwarbqbhom"

now =  dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open('quotes.txt', 'r') as quote_file:
        all_quotes = quote_file.readlines()
        quote = rd.choice(all_quotes)
    print(quote)

    try:
        # Use SMTP_SSL for port 465
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="oladimeji12344321@yahoo.com", 
                msg=f"Subject:Happy Birthday\n\n{quote}"
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")