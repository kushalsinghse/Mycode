try:
	p=int(input())
	o=[]
	for i in range(p):
		o.append(input())

	for i in o:
		i=i.split()
		print(int(i[0])%int(i[1]))

except:
	pass
