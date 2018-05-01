#!/usr/bin/python
from random import random, randint
from time import sleep
def count(fn):
	def _count(*largs, **kargs):
		_count.i += 1
		fn(*largs,**kargs)
	_count.i = 0
	return _count

def r_xor(p,q):
	#0000.0000.0000.0000
	#0000.0000.0000.1101 0000.0000.0001.1000
	#13,24
	r = p ^ q
	r = p
	i += 1
	print(i)
	print('{0:08b}'.format(r))
	sleep(.1)

	return (r_xor(r,q))
i = 0
p = randint(0,255)
q = randint(0,255)
print(p,q)
r_xor(p,q)
