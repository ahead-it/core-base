from core import *
from app import table


class UserProfile(Page):
    def _init(self):
        self._name = 'User Profile'
        self._caption = label('User Profile')
        self._insertallowed = False
        self._deleteallowed = False
        self.rec = table.User()

        if appctr := control.ContentArea(self):
            if gengrp := control.Group(appctr, label('General')):
                ctlid = control.Field(gengrp, self.rec.id)
                ctlid.enabled = False
                
                control.Field(gengrp, self.rec.name)

                control.Field(gengrp, self.rec.email)

                fldpwd = control.Field(gengrp, self.rec.password)
                fldpwd.type = control.FieldType.PASSWORD

    def _onload(self):
        self.rec.setfilterlevel(FilterLevels.PRIVATE)
        self.rec.id.setrange(Session.user_id)
        self.rec.setfilterlevel(FilterLevels.PUBLIC)


        