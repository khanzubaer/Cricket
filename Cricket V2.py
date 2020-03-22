import random

out = False
run = 0
totalrun = 0
batsman = 1
teamrun = 0

while (out==False):
    run = random.randint(0, 10)
    print("Batsman No: ", batsman)

    if(0<=run<=6):
        totalrun = run + totalrun
        print(run, "Runs")
    elif(run == 7):
        print("Run Out")
        batsman += 1
        print("Total run", totalrun, "\n")
    elif(run == 8):
        print("Catch Out")
        batsman += 1
        print("Total run", totalrun, "\n")
    elif(run == 9):
        print("Bowled Out")
        batsman += 1
        print("Total run", totalrun, "\n")
    elif(run == 10):
        print("Stump Out")
        batsman += 1
        print("Total run", totalrun, "\n")
    if(batsman == 11):
        out = True
        print("All Out")

teamrun = teamrun + totalrun
print("Team Run: ", teamrun)




