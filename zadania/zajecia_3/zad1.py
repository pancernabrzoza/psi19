a=[0,1,2,3,4,5,6]
b=[10,11,12,13,14,15,16]
def funkcja(a,b):
    c=[]
    for i,w in enumerate(a):
        if i%2==0:             
            c.append(w)
    for i,w in enumerate(b):
        if i%2==1:               
            c.append(w)
    print(c)
funkcja(a,b)

