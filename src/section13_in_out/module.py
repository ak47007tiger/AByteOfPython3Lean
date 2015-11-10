'''
Created on 2015年11月10日

@author: Peter
'''
import pickle

if __name__ == '__main__':
    print('abcdefg'[-1::-1])

file1 = open('file_test_io','r')
print(file1.readline())
file1.close()

file2 = open('file_store','wb')
pickle.dump(['a',1,'b','light'],file2)
file2.close()


file2 = open('file_store','rb')
list1 = pickle.load(file2)
print(list1)

file2.close()