#encoding:utf-8
#Miller-Rabin算法用来检测是否是素数
#输入数字n必须是奇数

import random

def TwoFact(n):
	r=n-1
	s=0
	while r%2==0:
		r=r/2
		s=s+1
	return s, r
def isProbablePrime(n):
	x=TwoFact(n)
	for i in xrange(1, x[0]+1):
		a=random.randint(2, n-2)
		y=(a**x[1])%n
		if y!=1 and y!=n-1:
			j=1
			while j<=x[0]-1 and y!=n-1:
				y=(y*y)%n
				if y==1:
					return 0
				else:
					j=j+1
			if y!=n-1:
				return 0
	return 1

'''n=raw_input('Please input detected number:')
a=isProbablePrime(int(n))
if a:
	print 'Prime number'
else:
	print 'Composite number'
'''