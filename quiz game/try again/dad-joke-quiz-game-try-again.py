import time

print("Welcome to My Quiz!!")
playing = input("Do you want to play? (Yes or no) ")
#checks to make sure that the user enters in only letters
while True:
    if playing.isalpha():
        break
    else:
        print("Must answer yes or no")
        time.sleep(2)
        playing = input("Do you want to play? (yes or no) ")
        continue

#double checks that the user only enters yes or no
while (playing != "yes" and playing != "no"):
    print("please enter yes or no")
    time.sleep(2)
    playing = input("Do you want to play? (Yes or no) ")
    if playing.lower() =="yes":
        print("Awesome lets get started!!!")
        break
    else:
        continue

#Quits the game if they don't want to play
if playing.lower() =="no":
        print("Why did you come here?")
        quit()

#starts keeping score of the game
#keeps track of idk scores
else:
    score = 0
    try_again = 0
    idk_score = 0

print("Awesome lets get started!!!")
time.sleep(2)

# TODO use a function and reuse this code value
answer = input("What do sprinters eat before a race? (if not sure say idk) ")

while (answer != "nothing they fast"): 
    sec_chan=input("Would you like to try again? (yes or no) ")
    if sec_chan == "yes":
        print("Awesome Lets try this again!")
        break
    else:
        Print



#if answer.lower() == "nothing they fast": 
    #print("Thats Correct!! Look who has there dad hat on!")
    #time.sleep(2)
    #score += 1
#elif answer.lower() == "idk":
    #print("Nothing They Fast!!!")
    #time.sleep(2)
    #idk_score += 1
#else:
    #print("No nothing they fast XD Try to get the next one" )
    #time.sleep(2)

# TODO use a function and reuse this code value
answer = input("Air use to be free at the gas station, now its a $1.50. You know why? (if not sure say idk) ")
if answer.lower() == "inflation":
    
    print("Thats Correct!! Your really good at this, do you have some kids on the way?")
    time.sleep(2)
    score += 1
elif answer.lower() == "idk":
    print("Inflation!!! XD you'll definitely get the next one!!")
    time.sleep(2)
    idk_score += 1
else:
    print("No its because of inflation XD One more you got this!!!")
    time.sleep(2)

# TODO use a function and reuse this code value
answer = input("How did the man on the moon cut his hair? (if not sure say idk) ")
if answer.lower() == "he eclipse it":
    
    print("Thats Correct!! Your definitely a father!!")
    time.sleep(2)
    score += 1
elif answer.lower() == "idk":
    print("He Eclipse it!!! XD Try putting on some cargo shorts to help bring out your inner dad!!")
    time.sleep(2)
    idk_score += 1
else:
    print("Haha no he eclipse it")
    time.sleep(2)

#displays message for score and idk score and try again
if score == 3:
    print("You got all the questions correct!!!")
    time.sleep(2)
    print("Since you did so well here is one more dad joke")
    time.sleep(2)
    print("What do you call a busy waiter? A server! XD")
    time.sleep(2)
    print("Thank you for playing!!!")
elif score < 3 and idk_score <= 3 and try_again <= 3:
    print("Darn you didn't get all the questions correct :/ ")
    time.sleep(2)
    print("Go back and try to get all the answers correct! Theres a secret!!!")
    time.sleep(2)
    print("Thank you for playing!!")

#User should not see this but just in case there is something think of something when testing they will see this message
else:
    print("How are you seeing this? Go back and play correctly!!")
    quit()


# possible solutions 
# https://stackoverflow.com/questions/26961427/asking-the-user-if-they-want-to-play-again
#