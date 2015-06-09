#encoding:utf-8
#使用二进制算法的模指数运算
class ModExp(object):
	"""docstring for ModExp"""
	def __init__(self, bas, e, m):
		super(ModExp, self).__init__()
		self.bas=int(bas)
		self.e=int(e)
		self.m=int(m)
	def modExpFun(self):
		while self.bas==0 or self.e==0:
			return -1;
		k=0x40000000
		p=self.bas%self.m
		tmpbas=p
		while (self.e&k)==0:
			k>>=1
		k>>=1
		while k!=0:
			p=(p*p)%self.m
			if (self.e&k)!=0:
				p=(p*tmpbas)%self.m
			k>>=1
		return p

'''bas=raw_input('Please input Base Number:')
e=raw_input('Please input Index:')
m=raw_input('Please input Modulus:')
a=ModExp(bas, e, m)
b=a.modExpFun()
print 'resulat:', b'''