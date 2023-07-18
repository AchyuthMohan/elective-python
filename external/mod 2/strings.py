s="Hello achyuth"
res=''
# vowels=['A','E','I','O','U','a','e','i','o','u']
vowels='aeiouAEIOU'
for i in s:
    if i not in vowels:
        res+=i
print(res)