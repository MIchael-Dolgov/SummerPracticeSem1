import smtplib
from email.mime.text import MIMEText
from filelib import send_error_log
def send_email(sender_email, sender_password, recipient_email, subject, message):
    """Отправка сообщения"""
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        # Настройка SMTP-сервера
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Начинаем защищенное соединение
            server.login(sender_email, sender_password)  # Авторизуемся
            server.sendmail(sender_email, recipient_email, msg.as_string())  # Отправляем письмо
        print("Email sent successfully!")
    except Exception as e:
        send_error_log(f"Failed to send email: {e}")
