#
# Henddher Pedroza 
# (C) 2014
#
# GPL v3 License
#

import unittest
from dice import Dice, dice_descr_re

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

	for i in range(10):
		d = Dice('3d6+8')
		print d, d.roll()
		d = Dice('d2-5')
		print d, d.roll()
		d = Dice('d%')
		print d, d.roll()
