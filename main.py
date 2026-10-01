import random
number = random.randint(1,101)
print("Guess the number its from 0 - 100")
n = True
attempt = 1

while n:
    
    guess = int(input("Enter number :"))
    if guess > number :
        print("The number you guess was big ")
        attempt=attempt+1
    elif guess < number:
        print("The number you guess was small")
        attempt=attempt+1
    elif guess == number:
        print("The number you guess was correct")
        print(f"you guess the number in {attempt} attempt")
        n = False        
        
        
        