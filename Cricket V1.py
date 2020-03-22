import random

out = False
totalrun = 0
batsman = 1
while (out==False):
    run = random.randint(0, 10)
    if(0<=run<=6):
        totalrun = run + totalrun
        print(run, " Runs Scored: ")
    elif(run == 7):
        batsman = batsman + 1
        print("Run Out")
        out = True
    elif(run == 8):
        batsman = batsman + 1
        print("Catch Out")
        out = True
    elif(run == 9):
        batsman = batsman + 1
        print("Bowled Out")
        out = True
    elif(run == 10):
        batsman = batsman + 1
        print("Stump Out")
        out = True
print("Total Run: ", totalrun)




