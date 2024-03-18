num = int(input('Enter the number: '))

print('Following are the factors of the number ' + str(num) + ': ')

for i in range(1 , num + 1):
    if num % i == 0:
        print(i)
