def answer(n):
    if n < 0:
        return 0
    n = int(n)
    ans = 0
    while n > 1:
        # match last bit of n to determine even or odd
        if n & 1 == 0:
            n >>= 1
        elif n == 3  or ((n + 1) & n) > ((n - 1) & (n - 2)):
            n = n-1
        else:
            n = n+1
        ans=ans+1
    return ans

print answer("4") == 2
print answer("15") == 5
print answer("13") == 5
print answer("9") == 4
print answer("2") == 1
print answer("1") == 0