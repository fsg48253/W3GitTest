s=input()
# s="ABC123"
if s[:3]=="ABC":
    n=int(s[3:])
    if n< 350:
        if n != 316:
            print("Yes")
            exit()
print("No")