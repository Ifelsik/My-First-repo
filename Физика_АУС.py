
v_1, v_2=float(input('скорости \n')), float(input())
if v_2>v_1:
	print('Первое тело не догонит второе!')
else:
	m_1, m_2=float(input('массы \n')),float(input())
	v_I=(v_1*(m_1-m_2)+2*m_2*v_2)/(m_1+m_2)
	v_II=(v_2*(m_2-m_1)+2*m_1*v_1)/(m_1+m_2)
	print("v_1'=",v_I)
	print("v_2'=",v_II)