#
# Henddher Pedroza 
# (C) 2014
#
# GPL v3 License
#

import random
import re
import unittest

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
		
class Entry:
	def __init__(self, attrs):
		self.ac = attrs.get('AC', ('', 0))
	def AC(self):
		return self.ac
		
entries = [
           Entry({'AC' : ('deflection bonus', 1)}),
           Entry({'AC' : ('deflection bonus', 2)}),
           ]


class DiceTests(unittest.TestCase):
	def test_dice_descr_re(self):
		self.assertRegexpMatches('d4', dice_descr_re)
		self.assertEqual(('', '4', None, None, None), dice_descr_re.match('d4').groups())
		self.assertRegexpMatches('d12 + 5', dice_descr_re)
		self.assertEqual(('', '12', '+ 5', '+', '5'), dice_descr_re.match('d12 + 5').groups())
		self.assertRegexpMatches('20d10', dice_descr_re)
		self.assertEqual(('20', '10', None , None , None ), dice_descr_re.match('20d10').groups())
		self.assertRegexpMatches('d3- 5', dice_descr_re)
		self.assertEqual(('', '3', '- 5', '-', '5'), dice_descr_re.match('d3- 5').groups())
		self.assertRegexpMatches('2d12 + 2', dice_descr_re)
		self.assertEqual(('2', '12', '+ 2', '+', '2'), dice_descr_re.match('2d12 + 2').groups())
		self.assertRegexpMatches('3d8-1', dice_descr_re)
		self.assertEqual(('3', '8', '-1', '-', '1'), dice_descr_re.match('3d8-1').groups())
		self.assertRegexpMatches('d% + 7', dice_descr_re)
		self.assertEqual(('', '%', '+ 7', '+', '7'), dice_descr_re.match('d% + 7').groups())
		self.assertNotRegexpMatches('d1', dice_descr_re)	
		self.assertNotRegexpMatches('d', dice_descr_re)
		self.assertNotRegexpMatches('3d', dice_descr_re)
		self.assertNotRegexpMatches('d+1', dice_descr_re)
		self.assertNotRegexpMatches('d 1', dice_descr_re)
		self.assertNotRegexpMatches('d -', dice_descr_re)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(DiceTests)
	unittest.TextTestRunner(verbosity=2).run(suite)

	e = entries[0]
	print e.AC()

	for i in range(10):
		d = Dice('3d6+8')
		print d, d.roll()
		d = Dice('d2-5')
		print d, d.roll()
		d = Dice('d%')
		print d, d.roll()
