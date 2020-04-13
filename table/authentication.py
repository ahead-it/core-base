from core import label, Table, field


class Authentication(Table):
    def _init(self):
        self._name = 'Authentication'
        self._caption = label('Authentication')
        
        self.token = field.Code('Token', label('Token'), 50)
        self.userid = field.Code('User ID', label('User ID'), 50)
        self.createdon = field.DateTime('Created on', label('Created on'))
        self.expireat = field.DateTime('Expire at', label('Expire at'))

        self._setprimarykey(self.token)
              
