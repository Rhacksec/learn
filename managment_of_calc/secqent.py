import sys
factorial = lambda x: factorial(x - 1) * x if x > 1 else 1
s = sys.stdin.readline()
s2 = s.split(' ')
x=int(s2[0])
y=int(s2[1])
so = int(factorial(y)/((factorial(y-2))*(factorial(2))))
summa = x+x*y+so*x+2
sys.stdout.write(str(summa))