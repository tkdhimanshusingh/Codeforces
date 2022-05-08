s=input()
l=list(map(str,s.split('+')))
l.sort()
print('+'.join(l))
