x = int(input('Enter the number: '))

for i in range(1, x) :
    if i**2 == x:
        a = True
        break
    else:
        a = False

if a == True:
    print(str(x) + ' is a perfect square.')
else:
    print(str(x) + ' is not a perfect square.')
