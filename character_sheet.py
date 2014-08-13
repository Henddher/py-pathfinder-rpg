#
# Henddher Pedroza 
# (C) 2014
#
# GPL v3 License
#

from dice import Dice

class Entry:
	def __init__(self, attrs):
		self.ac = attrs.get('AC', ('', 0))
	def AC(self):
		return self.ac
		
entries = [
           Entry({'AC' : ('deflection bonus', 1)}),
           Entry({'AC' : ('deflection bonus', 2)}),
           ]

if __name__ == '__main__':

	e = entries[0]
	print e.AC()

	for i in range(10):
		d = Dice('3d6+8')
		print d, d.roll()
		d = Dice('d2-5')
		print d, d.roll()
		d = Dice('d%')
		print d, d.roll()
