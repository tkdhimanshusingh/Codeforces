for i in range(1,int(input())+1):
    p=list(input())
    typed=list(input())
    p1=set(p)
    t1=set(typed)
    if len(p1)==len(t1) and p1==t1:
        print("Case #",i,':'," ",len(typed)-len(p),sep='')
    else:
        print("Case #",i,':'," IMPOSSIBLE",sep='')
