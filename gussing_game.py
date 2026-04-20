import random

secret_number = random.randint(1, 100)

print("welcome to the number guessing game.....")
print("i have choosen number between 1 to 100..")

attempt = 0

while True:
    guess = int(input("enter your guess :"))
    attempt+=1
    if guess<=0:
        print("you are entered a negative number or 0")
    elif guess > secret_number:
        print("high guess....try again....!!")
    elif guess < secret_number:
        print("low guess....try again....!!")
    else :
        print(f" Congratulations!!....you get it right in {attempt} attempt.")
        break
else:
    print(f"Sorry! You've used all {max_attempts} attempts. The number was {secret_number}.")