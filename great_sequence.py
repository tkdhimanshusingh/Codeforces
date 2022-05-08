for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    l=list(map(int,input().split()))
    cnt=0
    s=set()
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]//l[i]==k and s.__contains__(l[j])==False:
                s.add(l[j])
                print(l[i],l[j],s)
            else:
                cnt+=1
    print(cnt)
