def palin(st):
    x=st
    size=print(len(st))
    y=[]
    for i in range(-1,-6,-1):
        y.append(st[i])
    if x==y:
        print("Palindrome.")
    else:
        print("Not Palindrome.")
palin([10,11,12,11,10])