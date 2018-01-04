import random
def get_word():
  words=['facebook', 'syntax', 'error', 'implement', 'computer', 'system', 'keyword', 'hacker', 'security', 'debug', 'company', 'cyber', 'technology', 'processor', 'chip', 'ram', 'speed', 'clock', 'progress', 'storage', 'charles', 'keyboard', 'snapdragon', 'output']
  return random.choice(words).upper()
def main():
  word=get_word()
  guesses=[]
  guessed=False
  print('The word contains',len(word),'letters!')
  while not guessed:
    text='Please enter one letter or a {} letter word'.format(len(word))
    guess=input(text)
    guess=guess.upper()
    if guess in guesses:
      print('You already have guessed' + guess + '"')
    elif len(guess)==len(word):
      guesses.append(guess)
      if guess==word:
        guessed=True
      else:
        print('Sorry that is incorrect')
    elif len(guess)==1:
      guesses.append(guess)
      res=check(word,guesses,guess)
      if res==word:
        guessed=True
      else:
        print(res)
    else:
      print('Invalid Entry!')
  print ('Yes it is right, you found ' +word+ ' in ', len(guesses), ' tries')
  again=input('Want to play again? Type y to play')
  again=again.upper()
  if (again=='Y'):
    main()
  else:
    print('Thank you for playing :)')

def check(word,guesses,guess):
  status=''
  match=0
  for letter in word:
    if letter in guesses:
      status+=letter
    else:
      status+='*'
    if letter==guess:
      match+=1
  if match > 1 :
        print ('you have gussed ', match, 'letter truly "'+ guess +'"'+'\'s')
  elif match == 1:
        print ('You found one correct letter!', guess) 
  else:
        print ('Cant find the letter in the word, try again.')
  return status
main()