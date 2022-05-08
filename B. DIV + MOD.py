for _ in range(int(input())):
    l,r,a=list(map(int,input().split()))
    ans=(r//a)+r%a
    temp=(r//a)*a-1
    if temp>=l:
        f_temp=(temp//a)+temp%a
        ans=max(ans,f_temp)
    print(ans)
