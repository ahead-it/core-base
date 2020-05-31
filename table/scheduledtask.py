from core import *
from app import option, table


class ScheduledTaskStatus(Option):
    DISABLED = 0, label('Disabled')
    READY = 1, label('Ready')
    RUNNING = 2, label('Running')
    ERROR = 3, label('Error')


class ScheduledTask(Table):
    def _init(self):
        self._name = 'Scheduled Task'
        self._caption = label('Scheduled Task')

        self.entryno = field.Integer('Entry No.', label('Entry no.'))
        self.entryno.autoincrement = True

        self.description = field.Text('Description', label('Description'), 50)
        self.parameters = field.Text('Parameters', label('Parameters'), 250)
        self.status = field.Option('Status', label('Status'), option.ScheduledTaskStatus)
        self.enabled = field.Boolean('Enabled', label('Enabled'))
        self.stoprequest = field.Boolean('Stop request', label('Stop request'))

        self.runonmonday = field.Boolean('Run on Monday', label('Run on Monday'))
        self.runontuesday = field.Boolean('Run on Tuesday', label('Run on Tuesday'))
        self.runonwednesday = field.Boolean('Run on Wednesday', label('Run on Wednesday'))
        self.runonthursday = field.Boolean('Run on Thursday', label('Run on Thursday'))
        self.runonfriday = field.Boolean('Run on Friday', label('Run on Friday'))
        self.runonsaturday = field.Boolean('Run on Saturday', label('Run on Saturday'))
        self.runonsunday = field.Boolean('Run on Sunday', label('Run on Sunday'))

        self.startingtime = field.Time('Starting time', label('Starting time'))
        self.endingtime = field.Time('Ending time', label('Ending time'))
        self.runeverysecs = field.Integer('Run every (secs)', label('Run every (secs)'))

        self.nextrun = field.DateTime('Next run', label('Next run'))
        self.lastrun = field.DateTime('Last run', label('Last run'))
        self.execno = field.Integer('Execution no.', label('Execution no.'))

        self.unittype = field.Option('Unit type', label('Unit type'), UnitType)
        self.unitname = field.Text('Unit name', label('Unit name'), 250)
        self.methodname = field.Text('Method name', label('Method name'), 250)

        self.sessionid = field.Code('Session ID', label('Session ID'), 50)
        self.workerid = field.Code('Worker ID', label('Worker ID'), 50)
        self.server = field.Code('Server', label('Server'), 100)
        self.instance = field.Code('Instance', label('Instance'), 50)

        self._setprimarykey(self.entryno)

    def cleanup(self):
        self.workerid.value = ''
        self.sessionid.value = ''
        self.server.value = ''
        self.instance.value = ''

    def addlog(self, type, description):
        log = table.ScheduledTaskLog()
        log.init()
        log.taskno = self.entryno.value
        log.type = type
        log.datetime = datetime.now()
        log.execno = self.execno.value

        try:
            d = (datetime.now(Session.timezone) - self.lastrun.value).total_seconds()
            if d > 0:
                log.duration = d
        except:
            print(Convert.formatexception())

        log.description = description
        log.insert()

    def calcnextrun(self):
        self.nextrun.value = None

        if not self.enabled.value:
            return

        if not (self.runonmonday.value or
                self.runontuesday.value or
                self.runonwednesday.value or
                self.runonthursday.value or
                self.runonfriday.value or
                self.runonsaturday.value or
                self.runonsunday.value):
            return

        if not self.startingtime.value:
            return

        every = self.runeverysecs.value
        if every == 0:
            every = 1

        st = datetime.now(Session.timezone)
        if self.lastrun.value and (self.lastrun.value > st):
            st = self.lastrun.value
        st = st.replace(microsecond=0)

        while True:
            day = False
            if (st.weekday() == 0) and self.runonmonday.value:
                day = True
            elif (st.weekday() == 1) and self.runontuesday.value:
                day = True
            elif (st.weekday() == 2) and self.runonwednesday.value:
                day = True
            elif (st.weekday() == 3) and self.runonthursday.value:
                day = True
            elif (st.weekday() == 4) and self.runonfriday.value:
                day = True
            elif (st.weekday() == 5) and self.runonsaturday.value:
                day = True
            elif (st.weekday() == 6) and self.runonsunday.value:
                day = True

            hour = False
            if (st.time() >= self.startingtime.value) and\
                ((self.endingtime.value is None) or (st.time() <= self.endingtime.value)):
                hour = True

            if (day and hour) and ((self.lastrun.value is None) or
                                   (st >= self.lastrun.value + timedelta(seconds=every))):
                break

            st += timedelta(seconds=1)

        self.nextrun.value = st
