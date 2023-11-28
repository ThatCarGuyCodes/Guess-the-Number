from random import*

x = int(randint(0,1000000))
y = 0

while True:
  y+=1
  guess = int(input("Guess a positive number under 1 million: "))
  if guess < 0:
    print("POSITIVE NUMBER")
    exit()
  elif guess > x:
    print("Too high")
  elif guess < x:
    print("Too low")
  elif guess == x:
    print("Correct! It took you",y,"guesses to get it right.")
    exit()
  else:
    print("Guess the NUMBER not letter")
