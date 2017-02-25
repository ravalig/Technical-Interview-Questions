def question1(source,target):
	source_len = len(source)
	target_len = len(target)
	source = source.lower()
	target = target.lower()

	if(target_len > source_len):
		return False
	else:
		source_dict = {}
		target_dict = {}

		for j in target:
			if(j not in target_dict):
				target_dict[j] = 1
			else:
				target_dict[j] += 1

		start = 0
		end = target_len

		while(end <= source_len):
			temp = source[start:end]
			temp_dict = {}
			for i in temp:
				if(i not in temp_dict):
					temp_dict[i] = 1
				else:
					temp_dict[i] += 1
			if(temp_dict == target_dict):
				return True
			else:
				start +=1
				end += 1
		return False


print(question1("udacity", "Da"))