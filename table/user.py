import hashlib
from core import *
from app import option


class User(Table):
    def _init(self):
        self._name = 'User'
        self._caption = label('User')
        
        self.id = FieldCode('ID', label('ID'), 50)
        self.name = FieldText('Name', label('Name'), 50)
        self.email = FieldCode('E-Mail', label('E-Mail'), 100)
        self.enabled = FieldBoolean('Enabled', label('Enabled'))
        self.password = FieldText('Password', label('Password'), 50)
        self.lastlogin = FieldDateTime('Last login', label('Last login'))

        self._setprimarykey(self.id)
              
    def _password_onvalidate(self):
        self.password = self.hashpassword(self.password.value)

    def hashpassword(self, pwd):
        return hashlib.sha1(pwd.encode('utf8')).hexdigest()