import logging
from Logging.customlogger import *
class Test:
  def logtest(self):
    logger=getCustomLogger(logging.DEBUG)
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

t=Test()
t.logtest()