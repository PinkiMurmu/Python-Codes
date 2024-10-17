# Some list operations


# Printing from 0 to 4

def give(a):
    for i in range(a):
        print(i)
give(5)

# Rversing a given list

def swaplist(newlist):
    size=len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp
    return newlist
newlist=[10,11,12,13,14,15]
print(swaplist(newlist))

# Printing my name one letter in one line

def palin(str):
    x=str
    for i in range(len(x)):
        print(x[i])
palin("Pinki Murmu")
print("\n")

# Print from 0 to 9 with loops, conditions, breaks and continue

for i in range(100):
    if i<10:
        print(i)
        continue
    if i>=9:
        print("Can't take more...")
        break
    else:
        break