from core import *
from app import table, option
import smtplib


class Mail(Codeunit):
    @staticmethod
    def sendmessage(msg):
        setup = table.MailSetup()
        if not setup.get():
            setup.error_notfound()

        setup.servicetype.test()

        if setup.servicetype.value == option.MailServiceType.SMTP:
            if setup.secure.value == option.MailServiceSecure.SSL:
                srv = smtplib.SMTP_SSL(setup.server.value, setup.port.value)
            else:
                srv = smtplib.SMTP(setup.server.value, setup.port.value)

            if setup.secure.value == option.MailServiceSecure.TLS:
                srv.starttls()

            if setup.authentication.value:
                srv.login(setup.username.value, setup.getpassword())

            srv.send_message(msg)
            srv.quit()
