from carro import FillUp

class MileageCalculator:
	### fillup list, which aggregates two values.
	fillup = []

	### debugging state.
	debug = False


	##
	# Constructor.
	# Opens filename and calls Reader for inputting the mileage re
	# Raises an exception if filename does not exist.
	#
	# @param filename mileage file name.
	#
	def __init__(self, filename):
		try:
			f = open(filename, "r")
		except IOError:
			print("Cannot open file %s for reading" % filename)
			raise
		self.Reader(f)
	##
	# Reads a file with mileage and gasoline per line.
	# Creates FillUp object for each line and inserts in the filleup list.
	#
	# @param f mileage file object.
	#
	def Reader(self, f):
		for line in f:
			tempwords = line.split(None)
			if len(tempwords) == 2:
				try:
					self.fillup.append(FillUp(float(tempwords[0]), float(tempwords[1])))
				except:
					print("Invalid reading: %s\n" % tempwords)
		f.close()


	##
	# Calculates the consumption of the k-th entry of fillup list.
	#
	# @param k fillup index.
	# @return (odometer[k]-odometer[k-1]) / gallons[k].
	#
	def consumption(self, k):
		if k < 1 or k >= len(self.fillup): return None
		
		previous = self.fillup[k-1].getOdometer()
		current = self.fillup[k].getOdometer()
		gallons = self.fillup[k].getGallons()

		if MileageCalculator.debug:
			print("current %f\nprevious%f\ngallons %f\n"%(current, previous, gallons))
		return (current-previous) / gallons


	##
	# Returns the consumption (in mi/gal) corresponding to each
	# entry of "fillup", by calling the method "consuption".
	#
	# @return a string: a series of consumptions.
	#
	def __repr__(self):
		sb = "Miles per gallons\n"
		for i in range(1, len(self.fillup)):
			sb += "Consump. %d: %.3f\n" % (i, self.consumption(i))
		return sb

	##
	# Returns the consumption (in km/lt) corresponding to each entry
	# of "fillup", by calling the method "consumption".
	#
	# 1 gallon = 3.7854118
	# 1 mile = 1.609344
	#
	# @return a string: a sereis of consumption.
	#
	def __str__(self):
		sb = "kilometers per litre\n"
		for i in range(1, len(self.fillup)):
			sb += "Consump. %d: %.3f\n" %(i, self.consumption(i)*1.609344 / 3.7854118)
		return sb



	
	