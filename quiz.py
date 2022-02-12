f = open("QuizScore.txt","x")
import time
from typing import NamedTuple
def startfunc():
    print ("Lets start")
def endfunc():
    print ("GoodBye",name)
print ("Hello and welcome to my Quiz")
time.sleep(0.5)
name = input("What is your name ")
print ("Welcome",name)
time.sleep(1)
while True:
    yes = input ("To start the game type Start and to exit the game type quit. ")
    if yes.lower() == "start":
        startfunc()
        break
    if yes.lower() == "exit":
        print ("Bye")
# While loop second if statement doesn't work correctly.
print ("Now then Lets continue")
time.sleep(0.5)
print ("There will be 5 questions.")
time.sleep(1)
print ("round 1!")
time.sleep(0.5)
print ("This round is on maths")
question1 = input ("What is 56x45? Please use comma ")
if question1 == "2,520":
    print("Well done",name)
    f.write("1")
else:
    print ("You are wrong ")
    print ("The answer was 2,520")
time.sleep(1)
print ("question 2")
answer2 = input ("What is the captial of Amercia? ")
if answer2.lower() == "Washington DC":
    print ("Well done you are correct",name)
    f.write ("1")
else:
    print ("you are wrong")
    print ("It is Washington DC")
time.sleep(1)
print ("Question 3")
time.sleep(0.5)
question3 = input("What year did Steve Jobs? ")
if question3.lower() == "2011":
    print ("Well Done",name)
    f.write("1")
else:
    print ("you are wrong it was 2011")
time.sleep(1)
print ("Question 4")
time.sleep(1)
answer4 = input("Who was the 26 Presient of the United States? (Last name only) ")
if answer4.lower() == "Roosevelt":
    print ("Well Done",name)
    f.write(1)
else:
    print ("Wrong, it was Roosevelt")
time.sleep(1)
print ("Last question")
time.sleep(0.5)
print ("Question 5")
time.sleep(0.5)
question5 = input("Who wrote the book The Taming of the Shrew? (Full Name) ")
if question5 == "William Shakespeare":
    print ("Well done",name)
else:
    print ("Wrong")
    print ("It was William Shakespear")
time.sleep(1)
print ("Thats it the end of the quiz")
time.sleep(1)
print ("And the score is")
time.sleep(2)
f.close()
f = open("QuizScore.txt","r")
print (f.read())
#could be improved by having like well done you did well or you did great or you did terrible like a 3<  well done. than system just a bit more than having 11111.
time.sleep(0.5)
print ("Well Done",name)
endfunc()
exit()










