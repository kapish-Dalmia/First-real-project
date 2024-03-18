x = int(input('Enter the number: '))

for i in range(2 , x):
    if x % i != 0 :
        a = True
    else:
        a = False
        break

if a == True:
    print(str(x) + ' is a prime number. ')      
else:
    print(str(x) + ' is a composite number.')
