import logging
import inspect

def getCustomLogger(level):
	loggername=inspect.stack()[1][3]
	logger=logging.getLogger(loggername)
	logger.setLevel(level)
	fileHandler=logging.FileHandler('test.log',mode='a')
	fileHandler.setLevel(level)
	formatter=logging.Formatter('%(asctime)s - %(name)s -%(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
	fileHandler.setFormatter(formatter)
	logger.addHandler(fileHandler)
	return logger

def test():
    logger=getCustomLogger(logging.DEBUG)

test()