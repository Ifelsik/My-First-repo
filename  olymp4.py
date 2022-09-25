s=int(input())
e=int(input())
N=int(input())
sp=[]
for i in range(N):
    sp.append(int(input()))
t_ao=abs(s-e)
n=sorted(sp)

mn_a=n[0]-s
mp_a=0
for i in range(N):
    if n[i]-s<=0 and n[i]>mn_a:
        mn_a=n[i]
    if n[i]-s>0:
        mp_a=n[i]
        break
if abs(mn_a-s)>abs(mp_a-s):
    t1=abs(mp_a-s)
else:
    t1=abs(mn_a-s)

mn_o=n[0]-e
mp_o=0
for i in range(N):
    if n[i]-e<=0 and n[i]>mn_o:
        mn_o=n[i]
    if n[i]-e>0:
        mp_o=n[i]
        print(n[i])
if abs(mn_o-e)>abs(mp_o-e):
    t2=abs(mp_o-e)
else:
    t2=abs(mn_o-e)

T=t1+t2+1
if T>t_ao:
	print(t_ao)
else:print(T)