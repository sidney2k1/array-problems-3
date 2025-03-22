def pushzerotoend(a,asize):
    zero=0
    nonzero=0
    while(nonzero!=asize):
        if a[nonzero]!=0:
            a[nonzero],a[zero]=a[zero],a[nonzero]
            zero+=1
        nonzero+=1
a=[1,0,234,43,754,0,7,0,0,0,2,3,8]
asize=len(a)
print(a)
pushzerotoend(a,asize)
print("array after pushing all zeroes to end")
print(a)