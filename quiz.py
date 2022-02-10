import time
print ("Hello and welcome to my Quiz")
time.sleep(1)
while True:
    yes = input ("If you want to start please type yes ")
    if yes.lower() == "yes":
        print ("Lets start")
        break
else:
    print ("Goodbye")
    exit()
# try and put a function above for both of the outcomes in the while loop
print ("Now then Lets continue")
time.sleep(0.5)



