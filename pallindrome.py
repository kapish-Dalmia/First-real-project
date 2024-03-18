a = int(input('Enter the number: '))

def pallindrome(a):
    num = str(a)[::-1]
    if int(num) == a:
        return True
    else:
        return False

if pallindrome(a) == True:
    print(str(a) + ' is a pallindrome.')
else:
    print(str(a) + ' is not a pallindrome.')
