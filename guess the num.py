import random    #importing random module to generate random number   
random.randint(1, 100) #specifyign the range
attempts = 0
system_variable = random.randint(1, 100)
print("Enter any number between 1 and 100")
number = int(input())
while attempts < 3:
    attempts += 1
    if number == system_variable:
        print("Correct")
        break
    else:
        if number < system_variable:
                print("Too low")
        else:
            if number > system_variable:
                print("Too high")
    number = int(input())
print("The system generated number was", system_variable)
print("Number of attempts:", attempts)