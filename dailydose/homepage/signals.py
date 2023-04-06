from django.db.models.signals import post_save
from django.dispatch import receiver
import smtplib
from .models import Email, NewsArticle

@receiver(post_save, sender=Email)
def send_email_on_user_creation(sender, instance, created, **kwargs):
    if created:

        latest_user = Email.objects.latest('id')
        user_email = latest_user.email
        print(f'registered user is---{user_email}')
        user_choice = latest_user.choices
        user_choice = [choice.lower() for choice in user_choice]
        print(user_choice)

        # getting news according to choice
        news = NewsArticle.objects.filter(news_category__in = user_choice)
        print("news fetched")
        for i in news:
            title = i.title.encode('utf-8')
            desc = i.description.encode('utf-8')
            url = i.url
            # Setting up SMTP server
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username =   "YOUR_EMAIL_ADDRESS"
            smtp_password =   "GENERATE_YOUR_PASSWORD"   #go to myaccounts.google.com --> serach for App Passwords --> generate your password for mail
            smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
            smtp_conn.ehlo()
            smtp_conn.starttls()
            smtp_conn.login(smtp_username, smtp_password)

            # Set up the email message
            from_addr = "YOUR_EMAIL_ADDRESS"
            to_addr = user_email
            subject = f'{i.news_category} News'
            body = f"<strong>{title}</strong><br><br>{desc}<br><br>{url}<br>"
            msg = f'Content-Type: text/html;\nSubject: {subject}\n\n{body}'

            # Send the email
            smtp_conn.sendmail(from_addr, to_addr, msg)

            # Close the SMTP connection
            smtp_conn.quit()
            print(f'{i.news_category} news is sent successfully')



