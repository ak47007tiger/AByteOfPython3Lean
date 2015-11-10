q = 10
def function1(a,b = 2,c = 3):
    print('a is {0}'.format(a))
    global q
    a = q
    print('a is {0}'.format(a))
    print('b is {0}'.format(b))
    print('c is {0}'.format(c))
    d = 0
    def function2(e):
        nonlocal d
        print('d is {0}'.format(d))
        d = 4
        print('d is {0}'.format(d))
        print('e is {0}'.format(e))
    function2(6)
    print('d is {0}'.format(d))
function1(0,b = 8)

def function3(*arg1,**arg2):
    print(arg1)
    print(arg2)
function3((1,2,3),{'a':1,'b':2})
function3(1,2,3,4,a=1,b=2)

def function4(*arg1,b=3):
    print(arg1)
    print(b)
function4(1,2,3,b=4)

def function5(a,b,c):
    return a + b // c
print(function5(1, 2, 1))

def function6():
    global q
    q = 0
print(function6())

def function7():
    '''This is a function
test the docstring of python
    '''
    print('over')
print(function7.__doc__)

