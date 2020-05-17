import hashlib
from core import label, Table, field


class User(Table):
    def _init(self):
        self._name = 'User'
        self._caption = label('User')
        
        self.id = field.Code('ID', label('ID'), 50)
        self.name = field.Text('Name', label('Name'), 50)
        self.email = field.Text('E-Mail', label('E-Mail'), 100)
        self.enabled = field.Boolean('Enabled', label('Enabled'))
        self.password = field.Text('Password', label('Password'), 50)
        self.lastlogin = field.DateTime('Last login', label('Last login'))

        self._setprimarykey(self.id)
              
    def _password_onvalidate(self):
        self.password = self.hashpassword(self.password.value)

    def hashpassword(self, pwd):
        return hashlib.sha1(pwd.encode('utf8')).hexdigest()