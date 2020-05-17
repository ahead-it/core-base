from core import *
from app import table


class UserCard(Page):
    def _init(self):
        self._name = 'User Card'
        self._caption = label('User Card')
        self.rec = table.User()

        if appctr := control.ContentArea(self):
            if gengrp := control.Group(appctr, label('General')):
                control.Field(gengrp, self.rec.id)
                
                control.Field(gengrp, self.rec.name)

                control.Field(gengrp, self.rec.email)

                fldpwd = control.Field(gengrp, self.rec.password)
                fldpwd.type = control.FieldType.PASSWORD

                fldlst = control.Field(gengrp, self.rec.lastlogin)
                fldlst.enabled = False

                control.Field(gengrp, self.rec.enabled)


            

        