import random
print("Hello! What is your name?")
name = input()
print('Well ' + name + ' i am gonna pick a number from 1 to 100 and you have 10 tries to figure it out!\n Now, pick a number!')
number = random.randint(1, 100)

for i in range(0,10):
    guess = int(input())
    if guess < number:
        print('Your guess is too low!')
    elif guess > number:
        print('Your guess is too high!')
    else:
        break #this is the scenario where you guess the correct number!
      
if guess == number:
      print('You got it! Congrats!')
else:
      print('Better luck next time! The number I picked was: ' + str(number))
print('You took ' + str(i) + ' guesses')
