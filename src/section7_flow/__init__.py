i = int(input('enter a number'))
j = 5
if i > j and i <= 10:
    print('i > j')
    while i > 0:
        op = input('enter q to exit while')
        if op == 'q':
            break
        i -= 1
        print(i)
elif i < j and i > 0:
    print('i < j')
    for k in range(1,i):
        op = input('enter c to continue while')
        if op == 'c':
            continue
        print(k)
else:
    print('error number, 0 < number <= 10')
    
    