sum = 0

for i in range(1 ,11):
    x = eval(input('Enter the number: '))
    if type(x) == int :
        sum += x
    else:
        continue

print('The sum of only integers is ' + str(sum))
    
    
