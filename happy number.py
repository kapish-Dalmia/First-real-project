x = int(input('Enter the number : '))
lemg = len(str(x))
num = x

def happy(num):
    sum = 0
    for i in range(1 , lemg + 1):
        a = (num % 10) ** lemg
        sum += a
        num = num //10
    return sum

while True:
    if happy(num) != 1:
        num = happy(num)
        continue
    elif happy(num) == 1:
        print(str(x) + ' is a happy number.')
        break
    else:
        print(str(x) + ' is not a happy number.')
        break
