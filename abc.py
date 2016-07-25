### 20 blocks of alphabets will be given 
### blocks = [("B", "O"),("X", "K"),...,("Z", "M")]
blocks = [("B", "O"),
          ("X", "K"),
          ("D", "Q"),
          ("C", "P"),
          ("N", "A"),
          ("G", "T"),
          ("R", "E"),
          ("T", "G"),
          ("Q", "D"),
          ("F", "S"),
          ("J", "W"),
          ("H", "U"),
          ("V", "I"),
          ("A", "N"),
          ("O", "B"),
          ("E", "R"),
          ("F", "S"),
          ("L", "Y"),
          ("P", "C"),
          ("Z", "M")]

def canmakewordbyblock(word, block_of_words = blocks):
	
	flag = False

	if word == None:
		return True

	for char in word.upper:
		for block in block_of_words:
			if char in block:
				flag = True
			else:
				flag = False
				break

	if flag == True:
		return true
	else:
		return false					


	if __name__ == "__main__":
		

		print(", ".join("%s: %s" % (word, canmakewordbyblock(word)) for word in ["shan", "dae", "taek", "aa"]))			