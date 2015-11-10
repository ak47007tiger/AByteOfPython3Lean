zoo1 = (1,2,3)
list2 = ['a','b','c','d','e']
def func1():
    print('this is func1')
dic1 = {'a' : 1, 'b' : 'b str', 'c' : func1}
for key in dic1:
    print(key) 
print(dic1['a'])
dic1['c']()
print('1 - 3:',list2[1:3])
print(zoo1[0:2])
print(list2[-3:])
print(list2[0:-1:2])

set1 = set(list2)
print('a' in set1)
print(set(('a','b')) & set1)

set2 = {'a','b','c'}
print('set2:')
print(set2)

print(set1.issuperset(('a','b')))

print('start reference')
a = set1
print(a)
a = set2
print(a)
a = 1
print(a)
a = True
print(a)