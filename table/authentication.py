from core import label, FieldCode, FieldInteger, FieldOption, Option, Table, FieldDateTime
from app import option


class Authentication(Table):
    def _init(self):
        self._name = 'Authentication'
        self._caption = label('Authentication')
        
        self.token = FieldCode('Token', label('Token'), 50)
        self.userid = FieldCode('User ID', label('User ID'), 50)
        self.createdon = FieldDateTime('Created on', label('Created on'))
        self.expireat = FieldDateTime('Expire at', label('Expire at'))

        self._setprimarykey(self.token)
              
