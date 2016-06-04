k = raw_input()
test_cases = int(k)
for i in range(test_cases):
	a1 = raw_input()
	b1 = raw_input()
	a = [int(a1[i]) for i in xrange(len(a1))]
	b = [int(b1[i]) for i in xrange(len(b1))]
	n_0 = 0
	n_1 = 0
	if all(p==0 for p in a) or all(p==1for p in a):
		print 'Unlucky Chef'
	else:
		for x in xrange(len(a)):
			if a[x]!=b[x]:
					if a[x]==0:
						n_0+=1
					else:
						n_1+=1
		if n_0==n_1:
			print 'Lucky Chef'
			print n_0

		if n_0!=n_1:
			print 'Lucky Chef'
			print  max(n_0,n_1)
	