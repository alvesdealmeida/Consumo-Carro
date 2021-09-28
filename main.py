from carro import FillUp
from consumo import MileageCalculator
import sys
##
# Main method. Reads a series of pairs of mileage and number
# the average consumption: (current-previous) / gallons.
#
def main(argv=None):
	f = "mileage.txt"
	d = False
	if argv is None:
		argv = sys.argv

	if(len(argv) > 2):
		f = argv[1]
		d = argv[2] == "True"

	try:
		m = MileageCalculator(f)
		print(m)
		print(repr(m))
	except IOError:
		sys.exit("File %s not found." %f)

if __name__=="__main__":
	sys.exit(main())
		