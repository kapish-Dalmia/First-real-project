def hcf(x, y):
    if y > x:
        smaller = y
    else:
        smaller = x

    hcf = 1
    for i in range(1, smaller+1):
        if x % i == 0 and y % i == 0:
            hcf = i

    return hcf

def lcm(x,y):
    lcm = (x * y) / hcf(x,y)
    return lcm

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

print('The H.C.F. of the numbers is: ' + str(hcf(x,y)))
print('The L.C.M. of the numbers is: ' + str(lcm(x,y)))

