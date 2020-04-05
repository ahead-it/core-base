from core import *
from app import table, option


class SessionManagement(Codeunit):
    """
    System unit to handle session
    """
    def start(self):
        """
        Called when a session start
        """
        sess = table.Session()
        sess.init()
        sess.id = Session.id
        sess.type = self.getsessiontype()
        sess.address = Session.address
        sess.server = Session.hostname
        sess.processid = Session.process_id
        sess.datetime = datetime.now()
        sess.insert()

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