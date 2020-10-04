from core import *
from app import option


class MailServiceType(Option):
    NONE = 0, ' '
    SMTP = 1, 'SMTP'


class MailServiceSecure(Option):
    NONE = 0, ' '
    SSL = 1, 'SSL'
    TLS = 2, 'TLS'


class MailSetup(Table):
    def _init(self):
        self._name = 'Mail setup'
        self._caption = label('Mail setup')
        
        self.pk = field.Code('Primary key', label('Primary key'), 10)
        self.servicetype = field.Option('Type', label('Type'), option.MailServiceType)
        self.server = field.Text('Server', label('Server'), 100)
        self.port = field.Integer('Port', label('Port'))
        self.username = field.Text('Username', label('Username'), 100)
        self.password = field.Text('Password', label('Password'), 200)
        self.authentication = field.Boolean('Authentication', label('Authentication'))
        self.secure = field.Option('Secure', label('Secure'), option.MailServiceSecure)

        self._setprimarykey(self.pk)

    def _password_onvalidate(self):
        # FIXME use secret key
        if self.password.value:
            self.password = Convert.encryptstr(self.password.value, 'corebase')
        else:
            self.password = ''

    def getpassword(self):
        if self.password.value:
            return Convert.decryptstr(self.password.value, 'corebase')
        else:
            return ''

