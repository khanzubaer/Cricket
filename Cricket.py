import random

totalRun = 0
notOut = True
batsman = ("Tamim", "Liton", "Shakib", "Mushfiq", "Soumya", "Mahmud", "Meraj", "Mashrafee", "Mustafiz", "Saifuddin")

for i in range(len(batsman)):
    i += 1
    while (notOut):
        run = random.randint(0, 10)
        if (run == 7):
            notOut = False
            print("\nRun Out")
        elif (run == 8):
            notOut = False
            print("\nCatch Out")
        elif (run == 9):
            notOut = False
            print("\nBowled Out")
        elif (run == 10):
            notOut = False
            print("\nStump Out")
        elif (0 <= run <= 6):
            totalRun = totalRun + run
            print(run)
            print("Total Run: ", totalRun)
        else:
            print("\nOut")
            notOut = False