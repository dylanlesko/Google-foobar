def answer(xs):

    if len(xs) == 0:
        return 0

    product = 1
    pos = [val for val in xs if val > 0]
    neg = [val for val in xs if val < 0]
    neg = sorted(neg)
    
    if len(neg) == 1 and len(pos) == 0:
        return xs[0]
    if len(neg) == 0 and len(pos) == 0:
        return xs[0]


    if len(neg) % 2 == 0:
        for i in range(len(neg)):
            product = product * neg[i] 
    else:
        for i in range(len(neg)-1):
            product = product * neg[i] 
    
    for i in range(len(pos)):
        product = product * pos[i]
    
    return str(product)


print answer([])
print answer([2,0,2,2,0])
print answer([-2,-3,4,-5])
print answer([0,0,-42])
print answer([-3,-2,-4])
print answer([0,0])
print answer([0,0,4])
print answer([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000])