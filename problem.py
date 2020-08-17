try:
	x  = int(input())
	l = []
	score=0
	ns = [9,10,11]
	for i in range(x):
		y = int(input())
		for j in range(y):
			l.append(input())
		res=[0,0,0,0,0,0,0,0,0,0,0]
		for k in l:
			k = k.split()
			k = list(map(int,k))
			if(k[0] not in ns):
				res[k[0]] = max(res[k[0]],k[1])
		l=[]
		print(sum(res))
except:
	pass