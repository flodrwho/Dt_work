class Basketball:
	def __init__(self, name, games, goals):
		self.name = name
		self.games = games
		self.goals = goals
	def get_average(self):
		"""
		>>>b1 = Basketball("Karen", 20, 80)
		>>> b1.display_average()
		Player: Karen, Average goals per game: 4
		"""
		return self.goals / self.games
	def display_average(self):
		print("Player:", self.name(),", Average Goals per game: ", round(self.goals / self.games))
		
# main routine
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose = True)
	b1 = Basketball("Karen", 20, 80) 
	b1.display_average()
