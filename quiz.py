f = open("QuizScore.txt","x")
import time
def startfunc():
    print ("Lets start")
print ("Hello and welcome to my Quiz")
time.sleep(1)
while True:
    yes = input ("If you want to start please type yes ")
    if yes.lower() == "yes":
        startfunc()
        break
else:
    print ("Goodbye")
    exit()
# try and put a function above for both of the outcomes in the while loop
print ("Now then Lets continue")
time.sleep(0.5)
print ("There will be 5 questions.")
time.sleep(1)
print ("round 1!")
time.sleep(0.5)
print ("This round is on maths")
question1 = input ("What is 56x45 ")
if question1 == "2520":
    print("Well done")
    f.write("1")
else:
    print ("You are wrong ")
    print ("The answer was 2,520")
time.sleep(1)
print ("question 2")
answer2 = input ("What is the captial of Amercia")
if answer2.lower() == "Washington DC":
    print ("Well done you are correct")
    f.write ("1")
else:
    print ("you are wrong")





