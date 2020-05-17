from core import *
from app import table


class Information(Page):
    def _init(self):
        self._name = 'Information'
        self._caption = label('Information')
        self.rec = table.Information()

        if appctr := control.ContentArea(self):
            if gengrp := control.Group(appctr, label('General')):
                control.Field(gengrp, self.rec.name)
                
                control.Field(gengrp, self.rec.description)

                control.Field(gengrp, self.rec.copyright)
