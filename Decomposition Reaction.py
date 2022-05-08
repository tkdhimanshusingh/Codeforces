n,m=list(map(int,input().split()))
amount=list(map(int,input().split()))
for _ in range(m):
    decomposition_compound,n=list(map(int,input().split()))
    l=list(map(int,input().split()))
    i,j=0,1
    while j<len(l):
        quantity=l[i]
        product=l[j]
        amount[l[j]-1]=amount[l[j]-1]+amount[decomposition_compound-1]*l[i]
        i+=2
        j+=2
    amount[decomposition_compound-1]=0
for i in amount:
    print(i%(10**9+7))
