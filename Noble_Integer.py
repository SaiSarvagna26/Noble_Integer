def solve(A):
    A.sort()
    flag = -1
    j = 0
    for i in range(len(A)):
        j = i
        while j < len(A):
            if A[i] != A[j]:
                break
            j += 1
        if A[i] == len(A) - j:
            flag = 1
            break
    return flag

A=list(map(int,input().split()))
print(solve(A))