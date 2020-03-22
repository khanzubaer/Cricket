import random

out = False
run = 0
totalrun = 0
batsman = 1
teamrun = 0
balls = 0
overs = 0

while (out == False):
    run = random.randint(0, 10)
    print("Batsman No: ", batsman)
    balls = balls + 1

    if(0 <= run <= 6):
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
    if (balls % 6 == 0):
        overs = overs + 1
        print("Over finished: ", overs, "\n")
    if((batsman == 11) or (overs == 20)):
        out = True
        print("End of Innings")
        print("Total Overs Played: " + str(overs)+ "."+ str(balls % 6))
teamrun = teamrun + totalrun
print("Team Score: ", str(teamrun) + "/" + str(batsman-1))
runrate = teamrun/overs
print("Run Rate: ",round(runrate, 2))

print("\n\n**** Scorecard ****")
batting = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(batting)):
    i += 1
    print("Batsman",i, "scored",  "runs")