class FillUp:
	##
	# Odometer reading when the tank was filled.
	#
	odometer = 0.0

	##
	# Gallons needed to fill the tank.
	#
	gallons = 0.0

	##
	# Constructs a new FillUp object with the given data.
	# @param givenOdometer
	# odometer reading
	# @param givenGallons
	# number of gallons
	#
	def __init__(self, givenOdometer, givenGallons):
		self.odometer = givenOdometer
		self.gallons = givenGallons

	##
	# Returns the odometer reading.
	# @return
	# the odometer reading
	#
	def getOdometer(self):
		return self.odometer

	##
	# Returns the number of gallons.
	# @return
	# number of gallons
	#
	def getGallons(self):
		return self.gallons

	##
	#
