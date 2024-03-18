x = int(input('Enter the number: '))
num = x**2
leng = len(str(num))
sum = 0


for i in range(1 , leng +1 ):
    a = num % 10
    sum += a
    num = num//10

if sum == x:
    print(str(x) + ' is a neon number')
else:
    print(str(x) + ' is not a neon number')
    
