def translate(phrase):
	trans=""
	for letter in phrase:
		if letter.lower() in 'aeiou':
			if letter.isupper():
				trans=trans+"G"
			else:
				trans=trans+'g'
		else:
			trans=trans+letter
	return trans
print(translate(input('enter the phrase:')))
