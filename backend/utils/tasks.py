from instances.celery import celeryservice
from celery.schedules import crontab
from instances.mail import mail
from flask_mail import Message
from utils.mail import send_mail
import os
import time
from datetime import date  , datetime , timedelta
import csv
from application.models import User, Booking, Show
from instances.database import db
from datetime import date
from flask import render_template_string




@celeryservice.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    pass
    #periodic tasks
    # sender.add_periodic_task(20,test.s(),name="scheduled task == test_for_celery")
    # sender.add_periodic_task(2,dailyreport.s(),name="scheduled task == daily_report")
    sender.add_periodic_task(
        crontab(hour=23, minute=16),  
        user_reminder.s(),
        name="scheduled_task_user_reminder"
    )
    sender.add_periodic_task(
        crontab(hour=23, minute=16),  
        dailyreport.s(),
        name="dailyreport"
    )
    sender.add_periodic_task(
        crontab(day=21, hour=23, minute=16),  
        export_monthly_bookings.s(),
        name="monthlyreport"
    )



@celeryservice.task(name="mail to user")
def send_mail_task(receiver_email , subject , body):
    try:
        msg = Message(recipients=[receiver_email] , body=body,subject=subject)
        mail.send(msg)
        return 'registration mail sent'
    except Exception as e:
        return f'mail sending failed , reason : {e}'

@celeryservice.task(name="test_for_celery")
def test():
    return "hello! , celery is working."

@celeryservice.task(name="booking_reminder_for_users")
def user_reminder():
    today_date = date.today()
    users_without_bookings_today = User.query.filter(
        (User.role == "USER") &
            ~User.email.in_(
                db.session.query(Booking.user_id).filter(
                    Booking.booking_date == today_date
                )
            )
        ).all()
    if len(users_without_bookings_today) > 0:
        for user in users_without_bookings_today:
            receiver_email = user.email
            subject = "Booking Reminder"
            body = "You haven't booked a ticket today. Book one now!"
            try:
                msg = Message(
                    recipients=[receiver_email],  
                    body=body,
                    subject=subject
                    )
                mail.send(msg)
            except Exception as e:
                    print(f"Failed to send email to {receiver_email}: {e}")
        else:
            print("all users have booked ticket today.")
    return "User reminder task completed."
    
@celeryservice.task(name="export_monthly_bookings")
def export_monthly_bookings():
    try:
        now = datetime.now()
        month_year = now.strftime("%B_%Y")

        file_name = f"monthly_bookings_{month_year}.csv"
        file_path = os.path.join(os.getcwd(), file_name)

        bookings = Booking.query.filter(
            Booking.booking_date.between(
                now.replace(day=1),
                now.replace(day=1, month=now.month + 1) - timedelta(days=1)
            )
        ).all()

        with open(file_path, 'w', newline='') as csv_file:
            fieldnames = ['id', 'Tickets', 'show_id', 'user_id', 'booking_date']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for booking in bookings:
                writer.writerow({
                    'id': booking.id,
                    'Tickets': booking.Tickets,
                    'show_id': booking.show_id,
                    'user_id': booking.user_id,
                    'booking_date': booking.booking_date,
                })

        
        admin = User.query.filter(User.role == "ADMIN").first()
        admin_email = admin.email
        email_subject = f"Monthly Bookings Export - {month_year}"
        email_body = f"The monthly bookings for {month_year} have been exported and attached below."

        res = send_mail(admin_email, email_subject, email_body, file_path, "text/csv")

        return res
    except Exception as e:
        print(e)
        return False

@celeryservice.task(name="daily_report")
def dailyreport():
    try:
        today_date = date.today()

        # Query bookings made today
        bookings_today = Booking.query.filter_by(booking_date=today_date).all()
        # bookings_today = Booking.query.all()

        # Calculate total revenue
        total_revenue = 0
        for booking in bookings_today:
            show = Show.query.get(booking.show_id)
            revenue = int(booking.Tickets) * int(show.Price)
            total_revenue += revenue
        print(total_revenue)

        # Create an HTML report
        report_html = render_template_string(
            """
            <html>
            <head></head>
            <body>
                <h2>Daily Report - {{ today_date }}</h2>
                <p>Total Revenue: {{ total_revenue }} Rupees</p>
            </body>
            </html>
            """,
            today_date=today_date,
            total_revenue=total_revenue,
        )

        # Send the HTML report via email
        admin = User.query.filter(User.role == "ADMIN").first()
        recipient_email = admin.email
        subject = 'Daily Report'
        body = 'Please find the daily report below.'
        send_html_email(recipient_email, subject, body, report_html)

        return "Daily report generated and sent via email."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def send_html_email(recipient_email, subject, body, report_html):
    try:
        msg = Message(subject=subject, recipients=[recipient_email])
        msg.body = body
        msg.html = report_html
        mail.send(msg)
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

