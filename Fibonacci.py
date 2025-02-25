a=0
b=1
for i in range (0,10):
    if i==0:
        print(a)
    elif i==1:
        print(b)
    else:
        r=a+b
        t=b
        b=r
        a=t
        print(r)    
