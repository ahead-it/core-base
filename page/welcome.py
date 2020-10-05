from core import *
from app import page, table


class Welcome(Page):
    def _init(self):
        self._name = 'Welcome'
        self._caption = label('Welcome Page')

        if appctr := control.AppCenter(self):
            self.search = control.Search(appctr)

            self.usrcent = control.UserCenter(appctr)
            if self.usrcent:
                if actlist := control.ActionList(self.usrcent):
                    self.myprofile = control.Action(actlist, label('My Profile'), Icon.USER)
                    self.myprofile.description = label('Account settings and more')

                if actarea := control.ActionArea(self.usrcent):
                    self.signout = control.Action(actarea, label('Sign out'))

            self.navpane = control.NavigationPane(appctr)
            if self.navpane:
                self.dashboard = control.Action(self.navpane, label('Dashboard'), Icon.HOME)

                if settgrp := control.ActionGroup(self.navpane, label('Settings')):
                    if genact := control.Action(settgrp, label('General'), Icon.SETTINGS):
                        self.mailstp = control.Action(genact, label('Mail setup'))
                        self.actinfo = control.Action(genact, label('Information'))

                    if authact := control.Action(settgrp, label('Authentication'), Icon.USER):
                        self.actuser = control.Action(authact, label('Users'))

                    if sysact := control.Action(settgrp, label('System'), Icon.SYSTEM):
                        self.actsess = control.Action(sysact, label('Sessions'))

    def _onload(self):
        usr = table.User()
        usr.get(Session.user_id)
        self.usrcent.username = usr.name.value

    def _mailstp_click(self):
        stp = page.MailSetup()
        stp.run()

    def _actuser_click(self):
        usr = page.Users()
        usr.run()

    def _actinfo_click(self):
        nfo = page.Information()
        nfo.run()

    def _actsess_click(self):
        ses = page.Sessions()
        ses.run()

    def _signout_click(self):
        if Client.confirm(label('Sign out?')):
            Client.disconnect()
            

        