for _ in range(int(input())):
    s1=input()
    s2=input()
    f=0
    for i in range(len(s1)):
        #print(s1[i],i,len(s1)-i-1)
        if s1[i]==s2 and i%2==0 and (len(s1)-i-1)%2==0:
            f=1
            break
    if f==0:
        print("NO")
    else:
        print("YES")
