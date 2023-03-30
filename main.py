import random
import time

name = input("Who is you? ")

print ("Sup, " + name, "Wanna play a game?")

time.sleep(1)

print ("Hurry Up...")

time.sleep(0.5)


answer = random.randint(1, 19)
guesses = ''
turns = 3
while turns > 0:         
    failed = 0     


    for char in str(answer):      
        if char in str(guesses):    
              print (char,end=""),   
        else:
            print ("_",end=""),     
            failed += 1

   
    if failed == 0:        
        print (" was the number. You were just born better")
        break

    
    guess = int(input(" gimme a number:"))
    guesses += str(guess)           

    if guess < answer:
      print("LITTLE HIGHER")

    if guess > answer:
      print("LITTLE LOWER")

    if guess == answer:
      print("Noice")

  
    if guess != answer:  
        turns -= 1         
        print ("You have", + turns, 'more guesses' )
        if turns == 0:
            print("The number was " + str(answer))
            print ("You suck LOSER!!!!"  )
