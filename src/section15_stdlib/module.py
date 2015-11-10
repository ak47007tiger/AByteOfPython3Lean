'''
Created on 2015年11月10日

@author: mars
'''
import sys
import warnings
print(sys.api_version)
print(sys.version_info)

warnings.warn('this is a warning', RuntimeWarning)
print('program is running OK')

import os, platform, logging
logging_file = os.path.curdir + '/test.log'
print(platform.platform())
if platform.platform().startswith('Windows'):
    print('you work in windows')
else:
    print('you work in other')
    
logging.basicConfig(
level=logging.DEBUG, 
format='%(asctime)s - %(levelname)s - %(message)s', 
filename=logging_file, filemode='w')

logging.debug('debug msg')
logging.warning('debug msg')
logging.info('debug msg')

print(os.getcwd())
print(os.getcwdb())