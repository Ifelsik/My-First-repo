def centroid(n):
	c={'x':0, 'y':0}
	for i in range(n):
		print("Вершина", i+1)
		c['x']+=float(input('x: '))
		c['y']+=float(input('y: '))
	q={'x':c['x']/n, 'y':c['y']/n}
	return q