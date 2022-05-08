for _ in range(int(input())):
        n,q=list(map(int,input().split()))
        A=input()
        B=input()
        for _ in range(q):
                l,r=list(map(int,input()))
                if A[l-1:r]==B[l-1:r]:
                        print("YES")
                #To be used: print(l[l.index(str(a))+1-len(l)])
