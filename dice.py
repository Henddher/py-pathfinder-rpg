#
# Henddher Pedroza 
# (C) 2014
#
# GPL v3 License
#

import random
import re

dice_descr_re = re.compile(r'(\d*)d(2|3|4|6|8|10|12|20|%)\s*(([\+|\-])\s*(\d+))?')
		
class Dice:
	def __init__(self, descriptor):
		self.descriptor = descriptor
		self.multiplier, self.die, trash, const_sign, self.const = dice_descr_re.match(self.descriptor).groups()
		if self.multiplier == '':
			self.multiplier = 1
		else:
			self.multiplier = int(self.multiplier)
		if self.die == '%':
			self.die = 100
		self.die = int(self.die)
		if self.const != None:
			self.const = int(self.const)
		else:
			self.const = 0
		if const_sign == '-':
			self.const *= -1
	def roll(self):
		r = [random.randint(1, self.die)]
		for i in range(self.multiplier - 1):
			r.append(random.randint(1, self.die))
		return (r, sum(r) + self.const)
	def __str__(self):
		m = ''
		if self.multiplier > 1:
			m = self.multiplier
		d = self.die
		if self.die == 100:
			d = '%'
		s = '{}d{}'.format(m, d)
		if self.const != 0:
			s += '{:+}'.format(self.const)
		return s
		
