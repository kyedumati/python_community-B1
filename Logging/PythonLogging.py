import logging
logging.basicConfig(filename='../log.txt', level=logging.WARNING)
# logging.basicConfig(level=logging.WARNING)  #default level is warning
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y%I:%M:%S %p')
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')


import logging
logging.basicConfig(filename='mylog.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')
logging.info('A new Request Came')
try:
    x = int(input('Enter First Number:'))
    y = int(input('Enter Second Number:'))
    print('The Result:', x / y)

except ZeroDivisionError as msg:
    print('cannot divide with zero')
    logging.error(msg)
except ValueError as msg:
    print('Please provide int values only')
    logging.exception(msg)

logging.info('Request Processing Completed')
