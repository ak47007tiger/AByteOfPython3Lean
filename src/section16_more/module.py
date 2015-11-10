'''
Created on 2015年11月10日

@author: mars
'''
def m_repeater(n):
    return lambda s : s * n
twice = m_repeater(2)
print(twice('a'))
print(twice(3))

print('a' * 10) 

list1 = [1,2,3,4]
print([i ** 2 for i in list1 if i < 3])

exec("print('a' * 10)")

print(eval('[i ** 2 for i in list1 if i < 3]'))

a = int(input('enter a number > 0\n'))
try:
    assert a > 0
except AssertionError:
    print('want number > 0')
    
import logging
print(repr(logging))
print(repr(['item1',2,logging]))
