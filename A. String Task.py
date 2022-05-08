s=input()
vowels={'a','e','i','o','u','y'}
ans=''
for i in s:
    i=i.lower()
    if i not in vowels:
        ans=ans+'.'+i
print(ans)
