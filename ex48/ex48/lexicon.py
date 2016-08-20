class lexicon(object):
	
	def __init__(self):
		self.direction = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
		self.verb = ["go", "stop", "kill", "eat"]
		self.stop = ["the", "in", "of", "from", "at", "it"]
		self.noun = ["door", "bear", "princess", "cabinet"]
		self.dict1 = {"direction":self.direction, "stop":self.stop, "verb":self.verb, "noun":self.noun}

	def scan(self, stuff):
		words = stuff.split()
		result = []
		for word in words:
			errorFlag = True
			try:
				num = int(word)
				result.append(("number",num))
			except ValueError:					
				for type_word in self.dict1:
					word_set = self.dict1[type_word]
					for value_word in word_set:
						if word == value_word:
							result.append((type_word, word))
							errorFlag = False 
				if errorFlag == True:
					result.append(("error",word))
						
		return result


	def scan_1(self,stuff):
		words = stuff.split()
		result = []
		for word in words:
			errorFlag = True
			try:
				num = int(word)
				result.append(("number",num))
			except ValueError:
				flags = self.find_word(word)
				if flags[0] == True:
					result.append((flags[1],word))
				else:
					result.append((flags[1],word))
		return result

	def find_word(self,word):
		for type_word in self.dict1:
			word_set = self.dict1[type_word]
			for value_word in word_set:
				if word == value_word:
					return [True,type_word] 
		return [False,"error"]

