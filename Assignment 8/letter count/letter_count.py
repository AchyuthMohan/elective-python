def count(s):
    if len(s)==4:
        return True
    else:
        return False

f=open("words.txt","r")
s=f.read()
words=s.split()
for i in words:
    if count(i):
        print(i)
f.close()

