string=raw_input("enter your string: ")
count=0
if string.isdigit():
	print ('it is integer')
	count+=1
elif type(string) is str:
	new_str=string.split(' ')
	for i in new_str:
		if i.isdigit():
			print('integer in string')
			count+=1
			break
		else:
			pass
if count==0:
	print('this is string')