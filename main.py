def getmaxlength(a,asize):
    counter=0
    maximum=0
    for i in range(0,asize):
        if a[i]==0:
            counter=0
        else:
            counter+=1
            maximum=max(maximum,counter)
    return maximum
a=[1,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,1,1]
asize=len(a)
print("maximum consecutive 1's are:",getmaxlength(a,asize))    