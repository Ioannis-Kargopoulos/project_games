#Guesh game with While loop: user gives number he has 3 choises to find number.

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit :   #guess counts <=3
   guess = int(input("Guess: ")).  #user makes a guess
   guess_count += 1
   if guess == secret_number:
       print("You won!")
       break #Stopping the code.
else:         #else for while loop not for if
    print("Sorry you failed")