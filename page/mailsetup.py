from core import *
from app import table


class MailSetup(Page):
    def _init(self):
        self._name = 'Mail setup'
        self._caption = label('Mail setup')
        self.rec = table.MailSetup()

        if appctr := control.ContentArea(self):
            if gengrp := control.Group(appctr, label('General')):
                control.Field(gengrp, self.rec.servicetype)
                control.Field(gengrp, self.rec.server)
                control.Field(gengrp, self.rec.port)
                control.Field(gengrp, self.rec.secure)
                control.Field(gengrp, self.rec.authentication)
                control.Field(gengrp, self.rec.username)
                control.Field(gengrp, self.rec.password)

