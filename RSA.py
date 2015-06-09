import extended_Euclidean_algorithm as t3
import Miller_Rabin as t2
import Mod_Exp as t1
import random

def key():
	p=random.randint(2, 9999)
	q=random.randint(2, 9999)
	while t2.isProbablePrime(p)==0 or p%2==0:
		p=random.randint(2, 9999)
	while t2.isProbablePrime(q)==0 or q%2==0 or p==q:
		q=random.randint(2, 9999)

	n=p*q
	m=(p-1)*(q-1)
	e=random.randint(2, m-1)
	gcd=t3.eucInv(e, m)
	while gcd[0]!=1:
		e=random.randint(2, m-1)
		gcd=t3.eucInv(e, m)

	d=gcd[1]
	return n, e, d, p, q
	
def RSA_Encrypt(n, key):
	m=[]
	c=[]
	l=len(n)
	L=l
	while l>0:
		if l>=4:
			add=int(n[L-l])*(10**3)+int(n[L-l+1])*(10**2)+int(n[L-l+2])*10+int(n[L-l+3])
			m.append(add)
		else:
			last=0
			for i in xrange(l):
				last=last+int(n[L-i-1])*(10**i)
			m.append(last)
		l=l-4
	for i in xrange(len(m)):
		C=t1.ModExp(m[i], key[1], key[0])
		c.append(C.modExpFun())
		c[i]=str(c[i])
	c0=c[0]
	for i in xrange(1,len(m)):
		c0=c0+c[i]
	return c0, c, L

def RSA_Decrypt(c, key):
	m=[]
	for i in xrange(len(c[1])):
		M=t1.ModExp(c[1][i], key[2], key[0])
		m.append(M.modExpFun())
		m[i]=str(m[i])
	for i in xrange(len(m)-1):
		while len(m[i])<4:
			m[i]='0'+m[i]
	while len(m[-1])<c[2]%4:
		m[-1]='0'+m[-1]
	m0=m[0]
	for i in xrange(1,len(m)):
		m0=m0+m[i]
	return m0

k=key()
Encryption=raw_input('input:')
Decryption=RSA_Encrypt(Encryption, k)
Result=RSA_Decrypt(Decryption, k)
print 'Decryption:', Decryption[0], '\n', 'Encryption:', Result