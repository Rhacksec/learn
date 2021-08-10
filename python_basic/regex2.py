
import sys, re
pattern = r'(\w)(\1+)'
repl = r'\1'
for line in sys.stdin:
    print(re.sub(pattern, repl, line.rstrip()))
((1(01*0)*1|0)*)
#print(re.sub(r'\b[aA]+\w', 'computer',sys.stdin.read(), count=1 ), end='')

#pattern = r"z.{3}z"
#pattern = r"\\"
#[print(line.rstrip()) for line in sys.stdin if re.search(r'\b(\w+)\1\b', line)]
#sys.stdout.writelines(filter(re.compile(r"\b(\w+)\1\b").search, sys.stdin))
'''
pattern = r'\b[aA]+\w'
repl = 'computer'
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, repl, line, count=1)
    print(line)
'''




#print(re.sub(r'human', 'computer', sys.stdin.read()), end='')
#print(re.sub('human', 'computer',sys.stdin.read()))
#print(sys.stdin.read().replace('human', 'computer'))
'''
pattern = r"(.*)(cat)(.*)\2"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line) : print(line)
'''
#correct
'''
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(r"cat", line)) > 1:
        print(line)
'''
#\W+(cat)+\W
'''
pattern = r"\bcat\b"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line) : print(line)

'''