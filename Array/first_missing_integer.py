"""
Given an unsorted integer array, find the first missing positive integer.
Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1
"""
list = [int(num) for num in input().split()]
def missing_integer(list):
    dict={x:0 for x in list}
    for num in range(1,len(list)+1):
        if num not in dict:
            break
        else:
            num += 1
    return num

number = missing_integer(list)
print(number)


