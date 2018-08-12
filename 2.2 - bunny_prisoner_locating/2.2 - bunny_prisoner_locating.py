def answer(x, y):
    if x <= 0 or y <=0:
        return -1
    ans = 1 + ((y+y+x)*(x-1)/2) + (y * (y-1)/2)
    return str(int(ans))

print answer(1,1)
print answer(3,2)
print answer(2,3)
print answer(-1,1)