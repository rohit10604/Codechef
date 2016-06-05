import string
a_z = (string.ascii_lowercase)
k = raw_input()
n = int(k)
for x in range(n):
	s1 = raw_input()
	s = int(s1)
	answer=''
	n1 = s/26
	n2 = s%26
	for _ in range(n1):
		answer = answer + a_z
	answer = answer + a_z[0:n2]
	print answer
