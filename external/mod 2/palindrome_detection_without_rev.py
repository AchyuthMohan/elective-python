s="malayala"
i=0
j=len(s)-1
flag=0
while i<j:
    if s[i]==s[j]:
        i=i+1
        j=j-1
    else:
        flag=1
        i=i+1
        j=j-1
if flag==0:
    print("palindrome")
else:
    print("Not palindrome")