try:
       for _ in range(int(input())):
               n,x=list(map(int,input().split()))
               houses=list(map(int,input().split()))
               for i in range(1,len(houses)):
                   if houses[i]<x:
                       mx=i
               print(mx)
except:
        pass