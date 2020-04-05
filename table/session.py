from core import label, FieldCode, FieldInteger, FieldOption, Option, Table, FieldDateTime
from app import option


class SessionType(Option):
    CONSOLE = 0, label('Console')
    WEB = 1, label('Web')
    SOCKET = 2, label('Socket')
    BATCH = 3, label('Batch')


class Session(Table):
    def _init(self):
        self._name = 'Session'
        self._caption = label('Session')
        
        self.id = FieldCode('ID', label('ID'), 50)
        self.type = FieldOption('Type', label('Type'), option.SessionType)
        self.address = FieldCode('Address', label('Address'), 50)
        self.server = FieldCode('Server', label('Server'), 100)
        self.processid = FieldInteger('Process ID', label('Process ID'))
        self.datetime = FieldDateTime('Date/Time', label('Date/Time'))

        self._setprimarykey(self.id)
              
