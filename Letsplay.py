print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What is my nick name? ")
if answer == "Butu":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("What is my age? ")
if answer == "22":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
    
answer = input("What do i like the most? ")
if answer.lower() == "chocolate":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("Where do i like to travel? ")
if answer == "Beach":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
          
answer = input("What is my zodiac sign? ")
if answer.lower() == "virgo":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct :)")
print("You score " + str((score / 5) * 100) + "%.")

print( "Thankyou :)" )

