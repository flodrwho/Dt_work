class Movie:
	def __init__(self, Title, Producer, Director, Date, Length, Rating, Genre, Cost, Revenue):
		self.title = Title
		self.producer = Producer
		self.director = Director
		self.date = Date
		self.length = Length
		self.rating = Rating
		self.genre = Genre
		self.cost = Cost
		self.revenue = Revenue
	def display_data(self):
		print ("Title is ", self.title)
		print ("Producer is ", self.producer)
		print ("Director is ", self.director)
		print ("Date is ", self.date)
		print ("Length is ", self.length, " minutes")
		print ("Rating is ", self.rating)
		print ("Genre is ", self.genre)
		print ("Cost is ", self.cost, "dollars")
		print ("Revenue is ", self.revenue, "dollars")
	def net(self):
		print( self.revenue - self.cost)
m1 = Movie("The Book Thief", "TSG Entertainment", "Brian Percival", "February 4, 2013", 135,  7.6/10, "drama, war", 76086711, 19000000)	
m1.display_data()
m1.net()
