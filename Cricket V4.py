import random

print("\n*** Starting the Match ***\n")
country = {1: "Bangladesh", 2: "India"}
toss = random.randint(1, 2)

def game():
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
            print(run, "Run")
        elif(run == 7):
            print("Run Out")
            batsman += 1
            print("Total run:", str(totalrun) + "/" + str(batsman-1))
        elif(run == 8):
            print("Catch Out")
            batsman += 1
            print("Total run:", str(totalrun) + "/" + str(batsman-1))
        elif(run == 9):
            print("Bowled Out")
            batsman += 1
            print("Total run:", str(totalrun) + "/" + str(batsman-1))
        elif(run == 10):
            print("Stump Out")
            batsman += 1
            print("Total run:", str(totalrun) + "/" + str(batsman-1))
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
    print("Run Rate: ",round(runrate, 2), "\n")
    return teamrun

if (toss == 1):
    print(country[1], "won the toss & selected: Batting")
    score1 = game()
    print(country[2], "batting:")
    score2 = game()
elif (toss == 2):
    print(country[2], "won the toss & selected: Batting")
    score2 = game()
    print(country[1], "batting:")
    score1 = game()
if (score1 > score2):
    print(country[1], "has won the match by " + str(score1-score2)+ " runs")
elif (score2 > score1):
    print(country[2], "has won the match by " + str(score2-score1)+ " runs")
elif (score1 == score2):
    print("\nMatch Tied")




# print("\n\n**** Scorecard ****")
# batting = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(batting)):
#     i += 1
#     print("Batsman",i, "scored",  "runs")