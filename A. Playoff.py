n=int(input())
total=2**n
l=[x for x in range(1,total+1)]
i=0
j=1
while(j<=n):
    if (l[i]+l[j])%2==0:
        
