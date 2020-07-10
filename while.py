print("the animal with longest nose")
secret_word='elephant'
guess=""
count=0
while count<=4 and guess!=secret_word:
	guess=input('enter the guess:')
	count+=1
	
if guess==secret_word:
	print('you win!')
else:
	print("out of guess")
		
