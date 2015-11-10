'''
Created on 2015年11月10日

@author: mars
'''
class C:
    weight = 0
    def __init__(self,name):
        self.name = name
        C.weight += 1
    def __del__(self):
        C.weight -= 1
    def say(self):
        print('my name is',self.name)
obj = C('c')
obj.say()
print(C.weight)

class D(C):
    def move(self):
        print('moving')
    def stop(self):
        print('stop')
print(D.weight)
d = D('d')
d.say()
print(C.weight)