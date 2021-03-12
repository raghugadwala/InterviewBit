"""
Repeat and  Missing Number Array
"""
A = [int(num) for num in input().split()]
def repeatedNumber(A):
    size = len(A) + 1
    count = [0] * size
    for val in A:
        count[val] += 1

    repeat = missing = 0
    for index,value in enumerate(count):
        if value >= 2:
            repeat = index
        if value == 0 and index != 0:
            missing = index
    return repeat,missing

value=repeatedNumber(A)
print(value)