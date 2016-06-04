k = raw_input()
n = int(k)
for x in range(n):
	p1 = raw_input()
	p = int(p1)
	#print p
	y = raw_input().split()
	a=[int(l) for l in y]
	i=0
	value = "No"
	while i+2 < p:
		#print a[i],a[i+1],a[i+2]
		if a[i]==a[i+1]:
			#print "halfway"
			if a[i]==a[i+2]:
				value = "Yes"
				break
		i+=1
	print value