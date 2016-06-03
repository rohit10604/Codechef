z=raw_input().split()
n = int(z[0])
q = int(z[1])
z1=raw_input().split()
intlist = list(z1)
nums = [int(l) for l in intlist]
lowerlimit = min(nums)
upperlimit = max(nums)
for j in range(q):
	k = raw_input()
	t = int(k)
	print 'Yes' if lowerlimit <= t <= upperlimit else 'No'
