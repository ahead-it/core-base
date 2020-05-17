from core import *
from app import table, page


class Users(Page):
    def _init(self):
        self._name = 'Users'
        self._caption = label('Users')
        self.rec = table.User()
        self._cardpage = page.UserCard

        if appctr := control.ContentArea(self):
            if reptr1 := control.Repeater(appctr, label('User list')):
                control.Field(reptr1, self.rec.id)
                
                control.Field(reptr1, self.rec.name)

                control.Field(reptr1, self.rec.email)

                control.Field(reptr1, self.rec.enabled)
            

        