import logging
import logging.config
# logging.basicConfig(filename='./lx_log1.log')
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt=' %Y-%m-%d %H:%m:%S',
#                     filename='./lx_log1.log',
#                     filemode='w')
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# logger = logging.getLogger('kinslogger')
# print(logger.name)
# logger.setLevel(logging.INFO)

# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# fh=logging.FileHandler(filename='./lx_log1.log',mode='a',encoding='utf-8')
# fh.setLevel(logging.WARNING)

# formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)

# logger.addHandler(ch)
# logger.addHandler(fh)
logging.config.fileConfig('logglogging.conf')
logger = logging.getLogger('kinslogger')

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')


