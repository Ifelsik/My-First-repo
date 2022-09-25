def M(N):
	s=[0]*6
	k=0
	for i in range(2, N//2+1):
		if N%i==0:
			s[k]=i
			k+=1
		if k>4:
			break
	if k==5:
		return s[0]*s[1]*s[2]*s[3]*s[4]
	else:
		return 0

