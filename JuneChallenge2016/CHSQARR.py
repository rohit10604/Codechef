def cost(a,b,submatrix):
	max = 0
	sum = 0
	for x in submatrix :
		for y in x:
			sum = sum + y
			if y > max:
				max = y
	print (a+b)*max - sum
	
k = raw_input().split()
N = int(k[0])
M = int(k[1])
Matrix =[]
for x in xrange(N):
	s1 = raw_input().split()
	s = [int(w) for w in s1]
	Matrix.append(s)

k = raw_input()
n = int(k)
for x in xrange(n):
	w = raw_input().split()
	a = int(w[0])
	b = int(w[1])
print Matrix