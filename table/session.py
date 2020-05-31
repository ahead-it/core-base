from core import label, Option, Table, field
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
        
        self.id = field.Code('ID', label('ID'), 50)
        self.type = field.Option('Type', label('Type'), option.SessionType)
        self.address = field.Code('Address', label('Address'), 50)
        self.server = field.Code('Server', label('Server'), 100)
        self.instance = field.Code('Instance', label('Instance'), 50)
        self.processid = field.Integer('Process ID', label('Process ID'))
        self.datetime = field.DateTime('Date/Time', label('Date/Time'))
        self.userid = field.Code('User ID', label('User ID'), 50)

        self._setprimarykey(self.id)
              
