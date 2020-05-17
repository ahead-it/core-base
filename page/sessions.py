from core import *
from app import table, page


class Sessions(Page):
    def _init(self):
        self._name = 'Sessions'
        self._caption = label('Sessions')
        self.rec = table.Session()
        self._readonly = True

        if appctr := control.ContentArea(self):
            if reptr1 := control.Repeater(appctr, label('Session list')):
                control.Field(reptr1, self.rec.datetime)

                control.Field(reptr1, self.rec.userid)

                control.Field(reptr1, self.rec.type)
                
                control.Field(reptr1, self.rec.address)

                control.Field(reptr1, self.rec.server)

                ctlpid = control.Field(reptr1, self.rec.processid)
                ctlpid.visble = False
            

        