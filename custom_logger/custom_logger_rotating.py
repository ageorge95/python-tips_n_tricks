from sys import stdout
from logging import basicConfig, \
    INFO, DEBUG, WARNING, ERROR, CRITICAL, \
    Formatter, \
    getLogger, \
    StreamHandler
from concurrent_log_handler import ConcurrentRotatingFileHandler

def configure_logger():
    class CustomFormatter(Formatter):
        grey = "\x1b[38;21m"
        yellow = "\x1b[33;21m"
        red = "\x1b[31;21m"
        bold_red = "\x1b[31;1m"
        reset = "\x1b[0m"
        format = '%(asctime)s,%(msecs)d %(levelname)-4s' \
                 ' [%(filename)s:%(lineno)d ->' \
                 ' %(name)s - %(funcName)s] ___ %(message)s'

        FORMATS = {
            DEBUG: grey + format + reset,
            INFO: grey + format + reset,
            WARNING: yellow + format + reset,
            ERROR: red + format + reset,
            CRITICAL: bold_red + format + reset
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = Formatter(log_fmt)
            return formatter.format(record)

    ch = StreamHandler(stream=stdout)
    ch.setLevel(DEBUG)
    ch.setFormatter(CustomFormatter())
    fh = ConcurrentRotatingFileHandler('runtime_log.log',
                                       mode='a',
                                       maxBytes=20 * 1024 * 1024, #20 MB
                                       backupCount=2)
    fh.setLevel(DEBUG)
    fh.setFormatter(Formatter('%(asctime)s,%(msecs)d %(levelname)-4s'
                              ' [%(filename)s:%(lineno)d ->'
                              ' %(name)s - %(funcName)s] ___ %(message)s'))

    basicConfig(datefmt='%Y-%m-%d:%H:%M:%S',
                level=INFO,
                handlers=[
                    fh,
                    ch
                ])

if __name__ == '__main__':

    configure_logger()

    _log = getLogger()

    _log.info('info message')
    _log.warning('warning message')
    _log.error('error message')