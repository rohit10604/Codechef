def f1(a,b,i):
	value = a[i] * b[i]
	i = i+1
	return value

def f2(a,b):
	m = max(a)
	value = 0 ;
	indexlist = [i for i, j in enumerate(a) if j == m]
	for x in range(len(indexlist)):
		a[x] = a[x] - 1 ;
		if a[x]==0:
			del(a[x])

		value  = value + b[x]
	return value

def f1f2(a,b,i):
	answerlist=[0,0]
	while len(a) > 0 :
		for x in range(len(answerlist)):
			answerlist.append(x+f1(a,b,i))
			answerlist.append(x+f2(a,b))
			print answerlist
			if a[x]==0:
				del(a[x])

	print min(answerlist) + "rohit"

		



def kvalue(a):
	return max(a) - min(a)

k = raw_input()
test_cases = int(k)
for j in range(test_cases):
	z,n=raw_input().split()
	charlist = list(z)
	charset=set(z)
	flist = [charlist.count(x) for x in charset]
	flistsorted =sorted(flist,key=int)
	d = {x:flistsorted.count(x) for x in flistsorted}
	a = d.keys()
	b = d.values()

	while kvalue(a)<=n :
		i =0 ;
		f1f2(a,b,i)


	#print a
	#print b
	


