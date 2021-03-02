"""
Given a list of non negative integers, arrange them such that they form the largest number.
For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.
"""
num = [3, 30, 34, 5, 9]

def largestnumber(A):
    if not any(map(bool, A)):
        return '0'
    A = list(map(str, A))
    if len(A) < 2:
        return "".join(A)
    for x in range(len(A) - 1):
        y = x + 1
        while x < len(A) and y < len(A):
            if not int(A[x] + A[y]) > int(A[y] + A[x]):
                A[x], A[y] = A[y], A[x]
            y += 1
    return "".join(A)

n = largestnumber(num)
print(n)
