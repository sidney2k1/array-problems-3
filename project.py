a=[0,1,2,0,1,2,3,0,3,3,2,1,0,0,2,2,3,1,1,1]
zero=[]
one=[]
two=[]
three=[]
new=[]
for i in range(0,len(a)):
    if a[i]==0:
        zero.append(a[i])
    elif a[i]==1:
        one.append(a[i])
    elif a[i]==2:
        two.append(a[i])
    elif a[i]==3:
        three.append(a[i])
for i in range(0,len(zero)):
    new.append(zero[i])
for i in range(0,len(one)):
    new.append(one[i])
for i in range(0,len(two)):
    new.append(two[i])
for i in range(0,len(three)):
    new.append(three[i])
print("the old array:",a,"\nThe new sorted array:",new)