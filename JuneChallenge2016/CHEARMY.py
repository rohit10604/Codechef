def numberToBase(n, b):
    if n == 0:
        return 
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    #digits
    #print digits
    a2 = [str(x * 2) for x in digits]
    a3 =a2[::-1]
    a4 = "".join(a3)
    print a4

a = raw_input()
test_cases = int(a)
for b in range(test_cases):
	c = raw_input()
	k = int(c)
	k-=1
	if k==0:
		print 0
	else :
		numberToBase(k,5)