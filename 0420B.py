n,q=map(int,input().split(" "))
t=list(map(int,input().split(" ")))

# print(n,q)
# print(t)
a=[1 for i in range(n)]
for i,k in enumerate(t):
    if a[k-1]==1:
        a[k-1]=0
    else:
        a[k-1]=1
print(sum(a))