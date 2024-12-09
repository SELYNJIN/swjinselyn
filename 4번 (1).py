a=[0,1,2,3,4,5,6,7,8,9]
b=["A","B","C","D","E","F","G","H","I","J"]
c=[]
q=0
w=1
for i in range(4):
    w+=i
    c.extend(a[q:w])
    c.extend(b[q:w])
    q+=i
print(c)