import smtplib
from email.mime.text import MIMEText



with open("email.txt") as archivo :
    subject_numero = 0o0001
    for recipent in archivo:
        subject = f"Fwd: support issue #{subject_numero}"
        body = "waiting services"
        sender = "soporte.printware@gmail.com"
        recipients = recipent.strip()
        password = "vvlsecvwegorlcfh"
        subject_numero += 1
        def send_email(subject, body, sender, recipients, password):
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, recipients, msg.as_string())
            print("Message sent to:"+" "+ recipients)

        send_email(subject, body, sender, recipients, password)

print("Todos los emails fueron enviados correctamente")
##soporte.printware@gmail.com Captura1983