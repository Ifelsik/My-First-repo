def a(v):
	return -(0.4*v**2)/8
dt=5/1000
v=4
t=0
for i in range(1000):
	t+=dt
	v+=a(v)*dt
print(v)