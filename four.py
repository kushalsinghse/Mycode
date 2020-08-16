try:

	k = int(input())
	x = []
	for i in range(k):
		line = input()
		x.append(line)
	for i in x:
		print(i.count('4'))



except:
	pass