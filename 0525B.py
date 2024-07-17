s2=input()
s=list(map(int,input().split(" ")))
s2=list(map(int,input().split(" ")))

a = s + s2
a.sort()
# print(a)

for i in range(1, len(a)):
        if a[i] in s and a[i-1] in s:
                print("Yes")
                exit()
print("No")
        