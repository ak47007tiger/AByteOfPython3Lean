'''
Created on 2015年11月10日

@author: mars
'''
try:
    d = input('enter a number\n')
    a = 10 / int(d)
    print(a)
except EOFError:
    print('EOFError')
else:
    print('other section14_exception')

class MyE(Exception):
    def say(self = None):
        print('you cause a section14_exception')
try:
    if 'raise' == input('enter word'):
        raise MyE()
    else:
        print('run OK')
except MyE:
    MyE.say()
else:
    print('other e')
