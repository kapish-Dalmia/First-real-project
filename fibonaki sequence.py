x = int(input('upto where do you want the fibonaki sequence: '))

a = 0
b = 1

print('The fibonaki sequence upto ' + str(x) + ' is as following: ')
print('0 , 1 , ' , end = '')

for i in range(1 , x + 1):
    c = a + b
    a = b
    b = c
    print(c , end = ' , ')

print('...' , sep='')
