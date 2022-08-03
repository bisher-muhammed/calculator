a=1
f=1
n=int(input("enter number:"))
for a in range(f,n+1,a):
    f=f*a
    print(a)
    a=a+1
print ("factorial:",f)
