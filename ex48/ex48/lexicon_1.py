class lexicon_1(object):

	direction = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
	verb = ["go", "stop", "kill", "eat"]
	stop = ["the", "in", "of", "from", "at", "it"]
	noun = ["door", "bear", "princess", "cabinet"]
	dict1 = {"direction":direction, "stop":stop, "verb":verb, "noun":noun}	

	def __init__(self):
		pass
	
	@classmethod
	def scan(cls, stuff):
		words = stuff.split()
		result = []
		for word in words:
			errorFlag = True
			try:
				num = int(word)
				result.append(("number",num))
			except ValueError:					
				for type_word in lexicon_1.dict1:
					word_set = lexicon_1.dict1[type_word]
					for value_word in word_set:
						if word == value_word:
							result.append((type_word, word))
							errorFlag = False 
				if errorFlag == True:
					result.append(("error",word))
						
		return result

	@classmethod
	def scan_1(cls,stuff):
		words = stuff.split()
		result = []
		for word in words:
			errorFlag = True
			try:
				num = int(word)
				result.append(("number",num))
			except ValueError:
				flags = lexicon_1.find_word(word)
				if flags[0] == True:
					result.append((flags[1],word))
				else:
					result.append((flags[1],word))
		return result
	
	@classmethod
	def find_word(cls, word):
		for type_word in lexicon_1.dict1:
			word_set = lexicon_1.dict1[type_word]
			for value_word in word_set:
				if word == value_word:
					return [True,type_word] 
		return [False,"error"]

