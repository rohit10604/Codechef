import math
from math import factorial
def C(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)
a = raw_input().split()
test_cases = int(a[0])
for b in range(test_cases):
	n, k = raw_input().split()
	n = int(n)
	k = int(k)
	z1=raw_input().split()
	intlist = list(z1)
	nums = [int(l) for l in intlist if int(l)!=0]
	p = len(nums)
	if n==0:
		if k%2==0:
			print 1
		else:
			print 0

	if n!=0 and n==p:
		if k>=n:
			print (2**(n-1))%(10**9 + 7)
		else :
			if k%2==0:
				i= 0
				value = 0
				while i <= k:
				
					value = value + C(n,i)
					i+=2
				print (value%(10**9 + 7))
			else :
				j=1
				value2 = 0
				while j <=k:
				
					value2 = value2 + C(n,j)
					j+=2
				print (value2%(10**9 + 7))
	if n!=0 and n!=p:
		
		if k >=p:
			print ((2**p)%(10**9 + 7))
		else:
			m = 0
			value3 = 0
			while m <=k and m<=p:
				value3 = value3 + C(p,m)
				m+=1
			print (value3%(10**9 + 7))

				