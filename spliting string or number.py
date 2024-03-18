x = int(input('Enter the number: '))
leng = len(str(x))


def split(x):
    mid = leng // 2

    #even
    if leng % 2 == 0:
        first = str(x)[:mid]
        second = str(x)[mid:]
        return first , second

    #odd
    else:

        first1 = str(x)[:mid + 1]
        second1 = str(x)[mid + 1:]
        return first1 , second1


if leng % 2 == 0:
    first, second = split(x)
    print('The first half is ' + str(first))
    print('The second half is ' + str(second))

else:
    first, second = split(x)
    print('The first half is ' + str(first))
    print('The second half is ' + str(second))

