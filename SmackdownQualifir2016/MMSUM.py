def add(a,b):
	return a-b


k = raw_input()
test_cases = int(k)
for j in range(test_cases):
	max_so_far = 0
	max_ending_here = 0 
	max_so_farlist = 0 
	startindex = 0 
	endindex = 0
	currentstartIndex = 0
	index = -1
	value = 0 
	answerneg = 0 
	answerlist =[]
	k1 = raw_input()
	n=int(k1)
	z=raw_input().split()
	intlist = list(z)
	nums = [int(n) for n in intlist]
	answer_neg = max(nums)

	for x in nums:
		index = index+1
		max_ending_here = max_ending_here + x
		if max_ending_here<0:
			currentstartIndex = index+1
			max_ending_here = 0
			
		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			endindex = index
			startindex = currentstartIndex
			

	answerlist = nums[startindex:endindex+1]
	value = max_so_far
	#print answerlist
	if min(answerlist) < 0  and value > 0:
		value =add(value,min(answerlist))
		#max_so_far = max_so_far - min
	def ans():
		if answer_neg < 0:
			print answer_neg
		else:
			print value
	ans();