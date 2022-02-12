import logging
# logging.basicConfig(filename='log.txt')   #
# logging.basicConfig(level=logging.WARNING)  #default level is warning
# logging.basicConfig(filename='log.txt',format='%(asctime)s:%(levelname)s:%(message)s')
# logging.basicConfig(filename='log.txt',format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y%H:%M:%S %p')
# print('Logging Demo')
# logging.debug('Debug Information')
# logging.info('info Information')
# logging.warning('warning Information')
# logging.error('error Information')
# logging.critical('critical Information')

from Logging.customlogger import getCustomLogger

import logging
# logging.basicConfig(filename='mylog.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(funcName)s:%(message)s',
#                     datefmt='%d/%m/%Y %I:%M:%S %p')

logger=getCustomLogger(logging.DEBUG,'test')
logger.debug("testing debug")

def divide():
    logging.info('A new Request Came')
    try:
        x = int(input('Enter First Number:'))
        y = int(input('Enter Second Number:'))
        logging.info('The Result:', x / y)

    except ZeroDivisionError as msg:
        logging.error('cannot divide with zero')
        logging.error(msg)
    except ValueError as msg:
        print('Please provide int values only')
        logging.exception(msg)

    logging.info('Request Processing Completed')

divide()