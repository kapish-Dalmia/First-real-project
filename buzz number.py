x = int(input('Enter the number: '))
num = x


def buzz(num):
    leng = len(str(num))
    for i in range(1, leng + 1):
        a = num % 10
        num = num//10
        if a == 7:
            return True
        elif i == leng and a != 7:
            return False
        


if x % 7 == 0:
    print(str(x) + ' is a buzz number.')
else:
    if buzz(num) == True:
        print(str(x) + ' is a buzz number.')
    else:
        print(str(x) + ' is not a buzz number.')
