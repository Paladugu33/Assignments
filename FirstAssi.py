string=eval(raw_input("enter your string: "))
count=0
if type(string) is int:
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

'''

harshamohan@s10021-ThinkCentre-E73:~/Desktop/My$ python FirstAssi.py
enter your string: 10
it is integer
harshamohan@s10021-ThinkCentre-E73:~/Desktop/My$ python FirstAssi.py
enter your string: "harsha mohan"
this is string
harshamohan@s10021-ThinkCentre-E73:~/Desktop/My$ python FirstAssi.py
enter your string: "harsha mohan 434"
integer in string

'''