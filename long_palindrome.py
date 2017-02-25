def question2(test):
	length = len(test)
	pal_Length = 1
 
	start = 0 
	low = 0
	high = 0
	for i in range(1, length):
    	# Even
		low = i - 1
		high = i
		while low >= 0 and high < length and test[low] == test[high]:
			if high - low + 1 > pal_Length:
				start = low
				pal_Length=high-low + 1
			low -= 1
			high += 1
 
        # Odd
		low = i-1
		high = i+1
		while low>=0 and high<length and test[low]==test[high]:
			if high - low + 1 > pal_Length:
				start=low
				pal_Length = high-low + 1
			low -= 1
			high += 1
 
	result = test[start:start + pal_Length]
	return result

print(question2("nitin"))