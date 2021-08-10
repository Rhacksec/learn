
s = "abababacfgaba"
a = "aba"
b = "ba"
#s,a,b = input(), input(), input()
#print ('s>',s, 'a>', a, 'b>', b)
cnt, i = 0, 0
if len(a) == 1 : print(s.count(a))
elif s.count(a) == 0 : print('0')
else:
    for i in range(len(s)):
        if s[i:].startswith(a) : cnt += 1 
    print (cnt)

'''
replase_count = 0
while a in s:
    s=s.replace(a, b)
    replase_count += 1
    if replase_count > 1000 : break
if replase_count > 1000 : print('Imposisible')
else : print(replase_count)
'''