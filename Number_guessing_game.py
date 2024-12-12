import random
print("Hi welcome to the game,This game is about guessing the andom number between range 0 to 100.")
number_to_guess = random.randrange(100)
chances = 10
guess_counter = 0
while guess_counter <= chances:
    guess_counter +=1
    my_guess=int(input("Enter your number_to_guess:"))
    if my_guess == number_to_guess:
        print(f"The number is{number_to_guess}and you guesses right number!! well done!")
        break
    elif guess_counter > chances:
        print(f"The chances are over!good luck for next time.")
    elif my_guess < number_to_guess:
        print(f"your guess is less than the random number.")
    elif my_guess > number_to_guess:
        print(f"your guess is high than random nunber.")