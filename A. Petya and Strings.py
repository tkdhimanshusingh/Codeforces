s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
if len(s1)>len(s2):
    print(1)
elif len(s2)>len(s1):
    print(-1)
else:
    for i in range(len(s1)):
        if s1[i]>s2[i]:
            print(1)
            exit()
        elif s1[i]<s2[i]:
            print(-1)
            exit()
    print(0)
