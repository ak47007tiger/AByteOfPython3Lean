import sys
from sys import __stdin__
    
for i in sys.argv:
    print(i)
print(sys.argv)
print(__stdin__.read(1))


if __name__ == '__main__':
    print('this program is being run by itself')
else:
    print('i am imported from other module')