x = int(input('Enter the number: '))
mul = 1


for i in range(1 , x + 1):
    mul *= i

print('The factorial of ' + str(x) + ' is: ' + str(mul))
