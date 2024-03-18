x = int(input('Enter the number: '))
leng = len(str(x))
num = x
mul = 1
sum = 0


for i in range(1 , leng + 1):
    a = num % 10
    num = num//10
    for z in range(1 , a + 1):
        mul *= z
    sum += mul
    mul = 1

if sum == x:
    print(str(x) + ' is a special number.')
else:
    print(str(x) + ' is not a special number.')
        
