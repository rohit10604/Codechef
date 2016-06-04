from fractions import gcd
k = raw_input()
n = int(k)
for x in range(n):
	a,b,c,d = raw_input().split()
	g = gcd(int(c),int(d))
	a1 = (int(a)-int(b))%g
	a2 = (int(b)-int(a))%g
	print min(a1,a2)
