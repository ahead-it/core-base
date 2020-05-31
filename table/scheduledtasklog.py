from core import *
from app import option


class ScheduledTaskLogType(Option):
    START = 0, label('Start')
    COMPLETED = 1, label('Completed')
    ERROR = 2, label('Error')
    INFORMATION = 3, label('Information')


class ScheduledTaskLog(Table):
    def _init(self):
        self._name = 'Scheduled Task Log'
        self._caption = label('Scheduled Task Log')

        self.entryno = field.Integer('Entry no.', label('Entry no.'))
        self.entryno.autoincrement = True

        self.taskno = field.Integer('Task no.', label('Task no.'))
        self.execno = field.Integer('Execution no.', label('Execution no.'))

        self.type = field.Option('Type', label('Type'), option.ScheduledTaskLogType)
        self.datetime = field.DateTime('Date/time', label('Date/time'))
        self.duration = field.Integer('Duration (secs)', label('Duration (secs)'))

        self.description = field.Text('Message', label('Message'), 250)

        self._setprimarykey(self.entryno)
