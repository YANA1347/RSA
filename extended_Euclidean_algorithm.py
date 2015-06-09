#encoding:utf-8
#扩展欧几里德算法求乘法逆元

#返回的g表示最大公约数
def eucInv(a, m):
	if a==0 or m==0:
		return 0
	u=1
	g=a
	v1=0
	v3=m
	q=g/v3
	t3=g%v3
	while t3!=0:
		t1=(u-q*v1)%m
		u=v1
		g=v3
		v1=t1
		v3=t3
		q=g/v3
		t3=g%v3
	g=v3
	if g:
		if v1>0:
			return g, v1
		else:
			return g, m+v1
	else:
		return g, 0

'''x1=raw_input('Please input the int:')
x2=raw_input('Please input the mod:')
y=eucInv(int(x1), int(x2))
if y[1]==0:
	print 'Greatest common divisor:', y[0], 'no multiplicative inverse '
else:
	print 'Greatest common divisor:', y[0], 'multiplicative inverse:', y[1]'''