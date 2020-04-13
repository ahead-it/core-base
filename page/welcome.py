from core import *


class Welcome(Page):
    def _init(self):
        self._name = 'Welcome'
        self._caption = label('Welcome Page')

        if appctr := control.AppCenter(self):
            if actarea := control.ActionArea(appctr):
                if actcomp := control.Action(actarea, label('Components')):         
                    pass

                if actappl := control.Action(actarea, label('Applications')):            
                    pass

                if actcust := control.Action(actarea, label('Custom')):
                    if acterrs := control.Action(actcust, label('Error Pages'), 'fa-exclamation-triangle'):
                        self.error1 = control.Action(acterrs, label('Error 1'))
                        self.error2 = control.Action(acterrs, label('Error 2'))
                        self.error3 = control.Action(acterrs, label('Error 3'))

                    if actwiza := control.Action(actarea, label('Wizard'), 'fa-magic'):
                        pass

            self.search = control.Search(appctr)

            if usrcent := control.UserCenter(appctr):
                if actlist := control.ActionList(usrcent):
                    self.myprofile = control.Action(actlist, label('My Profile'), 'fa-user')
                    self.myprofile.description = label('Account settings and more')

                    self.mymessages = control.Action(actlist, label('My Messages'), 'fa-envelope-o')
                    self.mymessages.description = label('Inbox and tasks')

                if actarea := control.ActionArea(usrcent):
                    self.signout = control.Action(actarea, label('Sign out'))
                        
            if navpane := control.NavigationPane(appctr):
                self.dashboard = control.Action(navpane, label('Dashboard'), 'fa-home')

                if applgrp := control.ActionGroup(navpane, label('Applications')):
                    if ecommr := control.Action(navpane, label('eCommerce'), 'fa-shopping-cart'):
                        self.customers = control.Action(navpane, label('Customers'))
                        self.products = control.Action(navpane, label('Products'))

    def _error1_click(self):
        if Client.confirm('Continue?'):
            Client.message('Continue YES')        
        else:
            Client.message('BREAK')        
                        
    def _error2_click(self):
        Client.message('Error 2 pressed')        

    def _error3_click(self):
        Client.message('Error 3 pressed')        

    def _search_search(self, what):
        Client.message('You searched: ' + what)

            

        