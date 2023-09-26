1
def countDown(num1):
    list = []
    for i in range(num1, -1, -1):
        list.append(i)
    return list

print(countDown(5))

2
def printReturn(list):
    print(list[0])
    return list[1]

numbers = [3, 4]
print(printReturn(numbers) + 4)

3
def firstPlusLength(list):
    return list[0] + len(list)

numbers = [5, 5, 5, 5, 5]
print(firstPlusLength(numbers))

4
def valuesGreater(list):
    newlist = []
    if len(list) < 2:
        return False 
    for idx, val in enumerate(list):
        if val> list[1]:
            newlist.append(val)
    print(len(newlist))
    return newlist
print(valuesGreater([5,2,3,2,1,4]))

5
def thisLength(size, value):
    newlist = []
    for i in range(0, size):
        newlist.append(value)
    return newlist

print(thisLength(7, 4))
