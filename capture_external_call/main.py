from subprocess import PIPE,\
    Popen
from threading import Thread
from logging import getLogger
from typing import AnyStr
from custom_logger.custom_logger_rotating import configure_logger

level_descriptor = {'stdout': 'info',
                    'stderr': 'error'}

class Execute_and_capture():
    '''
    Class in charge with executing an external command and capturing its stderr and stdout into a custom logger
    '''
    def __init__(self,
                 cmd: list,
                 cwd: AnyStr = None,
                 _log: getLogger = None
             ):
        self.cmd: list = cmd
        self.cwd: AnyStr = cwd
        self._log = _log if _log else getLogger()

    def slave_x(self,
                x: AnyStr):
        for out in zip(iter(getattr(self.popen, x).readline, "")):
            yield out
        getattr(self.popen, x).close()

    def delegate_x(self,
                   x: AnyStr):
        for output in self.slave_x(x):
            getattr(self._log, level_descriptor[x])(output)

    def execute(self):
        args = {'args': self.cmd,
                'stdout': PIPE,
                'stderr': PIPE,
                'universal_newlines': True}
        if self.cwd:
            args.update({'cwd': self.cwd})
        self.popen = Popen(**args)

        for target in [lambda : self.delegate_x('stdout'),
                       lambda : self.delegate_x('stderr')]:
            Thread(target=target).start()

        return_code = self.popen.wait()
        self._log.info(f'Execution finished with exit code {return_code}')

if __name__ == '__main__':

    configure_logger()

    Execute_and_capture(
        cmd=['python', 'external_call_mockup.py']
    ).execute()