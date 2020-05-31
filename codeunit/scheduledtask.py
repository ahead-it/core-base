from core import *
from app import table, option


class ScheduledTask(Codeunit):
    def runtask(self, workerid, entryno):
        tasks = table.ScheduledTask()
        tasks.get(entryno)
        tasks.workerid = workerid
        tasks.sessionid = Session.id
        tasks.server = Session.hostname
        tasks.instance = Session.instance
        tasks.modify()
        commit()

        un = 'app.' + UnitType.name(tasks.unittype.value).lower() + '.' + tasks.unitname.value

        proxy = Proxy(un)
        proxy.create()
        return proxy.invoke(tasks.methodname.value, tasks)

    def dispatch(self):
        # Run tasks
        tasks = table.ScheduledTask()
        tasks.locktable()
        tasks.enabled.setrange(True)
        tasks.status.setrange(option.ScheduledTaskStatus.READY)
        tasks.nextrun.setfilter('<>{0}&<={1}', None, datetime.now())
        while tasks.findfirst():
            tasks.status.value = option.ScheduledTaskStatus.RUNNING
            tasks.lastrun.value = datetime.now(Session.timezone)
            tasks.execno.value += 1
            tasks.modify()

            tasks.addlog(option.ScheduledTaskLogType.START, label('Task {0} started'.format(tasks.description.value)))

            commit()

            Task.run('app.codeunit.ScheduledTask', 'runtask', None, tasks.entryno.value)

        # Get results
        tasks.locktable(False)
        tasks.reset()
        tasks.status.setrange(option.ScheduledTaskStatus.RUNNING)
        tasks.server.setrange(Session.hostname)
        tasks.instance.setrange(Session.instance)
        if tasks.findset():
            while tasks.read():
                # Kill?
                if tasks.stoprequest.value:
                    Task.kill(tasks.workerid.value)
                    tasks.stoprequest = False
                    tasks.modify()
                    commit()
                    continue

                try:
                    if Task.getresult(tasks.workerid.value) is None:
                        continue

                    tasks.addlog(option.ScheduledTaskLogType.COMPLETED,
                                 label('Task {0} completed'.format(tasks.description.value)))
                except:
                    error = Convert.formatexception()
                    tasks.addlog(option.ScheduledTaskLogType.ERROR,
                                 error['message'])

                tasks.status.value = option.ScheduledTaskStatus.READY
                tasks.lastrun.value = datetime.now(Session.timezone)
                tasks.cleanup()
                tasks.calcnextrun()
                tasks.modify()
                commit()
