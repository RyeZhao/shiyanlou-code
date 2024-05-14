def have7(num):
	if (num%10==7) or (num//10==7):
		return 1 
	else:
		return 0
def mul7(num):
	if num%7==0:
		return 1
	else:
		return 0

for i in range(1,101):
	if have7(i) or mul7(i):
		continue
	else:
		print(i)