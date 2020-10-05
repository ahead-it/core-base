from core import *
from app import table, option


class SessionManagement(Codeunit):
    """
    System unit to handle session
    """

    def server_start(self):
        """
        Once when server start
        """
        sess = table.Session()
        sess.server.setrange(Session.hostname)
        sess.deleteall()
        commit()

    def start(self):
        """
        Called when a session start
        """
        auth = table.Authentication()
        auth.reset()
        auth.expireat.setfilter('..{0}', datetime.now())
        if not auth.isempty():
            auth.deleteall()

        if Session.auth_token > '':
            auth = table.Authentication()
            auth.token.setrange(Session.auth_token)
            auth.expireat.setfilter('{0}..', datetime.now())
            if auth.findfirst():
                auth.expireat = datetime.now() + timedelta(hours=1)
                auth.modify()

                Session.authenticated = True
                Session.user_id = auth.userid.value

        sess = table.Session()
        sess.init()
        sess.id = Session.id
        sess.type = self.getsessiontype()
        sess.address = Session.address
        sess.server = Session.hostname
        sess.instance = Application.instance['name']
        sess.processid = Session.process_id
        sess.datetime = datetime.now()
        sess.userid = Session.user_id
        sess.insert(True)

    def stop(self):
        """
        Called when a session ends
        """
        sess = table.Session()
        if sess.get(Session.id):
            sess.delete()

    def getsessiontype(self):
        """
        Converts string type session to option value
        """
        if Session.type == 'cli':
            return option.SessionType.CONSOLE
        elif Session.type == 'web':
            return option.SessionType.WEB
        elif Session.type == 'socket':
            return option.SessionType.SOCKET
        elif Session.type == 'batch':
            return option.SessionType.BATCH
        else:
            error(label('Unknown session type \'{0}\''.format(Session.type)))

    @PublicMethod
    def login(self, email, password, remember=False):
        """
        Authenticate user (has a COMMIT)
        """
        user = table.User()
        user.reset()
        if not user.isempty():
            user.email.setrange(email)
            user.password.setrange(user.hashpassword(password))
            if not user.findfirst():
                error(label('Invalid e-mail or password!'))

        sess = table.Session()
        if not sess.get(Session.id):
            sess.error_notfound()
        sess.userid = user.id.value
        sess.modify(True)

        if Session.auth_token > '':
            auth = table.Authentication()
            if not auth.get(Session.auth_token):
                auth.init()
                auth.token.value = Session.auth_token
                auth.userid = user.id
                auth.createdon = datetime.now()
                auth.insert()
            
            if remember:
                auth.expireat = datetime.now() + timedelta(days=90)
            else:
                auth.expireat = datetime.now() + timedelta(hours=1)
            auth.modify()

            Client.save_auth_token(auth.expireat.value)

        commit()

        Session.authenticated = True
        Session.user_id = user.id.value

    @PublicMethod
    def initialize(self):
        """
        Returns generic parameters for the client
        """
        info = table.Information()
        info.get()

        return {
            'background': 'background.png',     # FIXME
            'logo': 'logo.png',                 # FIXME
            'logo_small': 'logo_small.png',     # FIXME
            'icon': 'icon.png',                 # FIXME
            'name': info.name.value,
            'description': info.description.value,
            'copyright': info.copyright.value,
            'indicator': info.indicator.value,
            'authenticated': Session.authenticated,
            'startpage': 'app.page.Welcome',

            'label_signin': label('Sign in'),
            'label_pwdlostqst': label('Password lost?'),
            'label_email': label('E-Mail'),
            'label_password': label('Password'),
            'label_pwdlost': label('Password lost'),
            'label_back': label('Back'),
            'label_send': label('Send'),
            'label_credentials': label('Insert your credentials'),

            'style_title': 'color: #000000'
        }            
        