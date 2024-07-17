s=list(map(int,input().split(" ")))
sus=[1,2,3]

for i in s:
     if i in sus :
        sus.remove(i)   

a= (sus[0] if len(sus) == 1 else -1)
print(a)