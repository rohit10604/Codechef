k = raw_input()
n_cities = int(k)
a = raw_input().split()
#cities = [int(x) for x in a]
n_queries = raw_input()
n =int(n_queries)
for t in range(n):
	s1 = raw_input().split()
	if int(s1[0])==1:
		p = int(s1[1])
		f = int(s1[2])
		a[p-1]=f
	else:
		value = 1
		R = int(s1[1])
		i = 0
		while i*R+1<=n_cities:
			value = value * int(a[i*R])
			i+=1
		answer = str(value)
		print answer[0],value%(7+10**9)
	 