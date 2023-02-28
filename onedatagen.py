import random

# Table 3: Bowler, Batsmen, outcome
table_3 = [[random.choice(["Bowler {}".format(i) for i in range(1, 6)]),
            "Player {}".format(random.randint(1, 11)),
            random.choice(["Out", random.randint(0, 10), random.randint(0, 10)])]
           for i in range(50)]

# Table 2: Bowler, runs, overs, wickets, average
table_2 = [["Bowler {}".format(i), 0, 0, 0, 0] for i in range(1, 6)]

# Table 1: Player name, Runs, Balls, 4s, 6s, Out by
table_1 = [["Player {}".format(i), 0, 0, 0, 0, ""] for i in range(1, 12)]
wickets = 0

for i, row in enumerate(table_3):
    bowler, batsman, outcome = row
    if outcome == "Out":
        wickets += 1
        table_1[int(batsman.split()[-1])-1][5] = bowler
    else:
        table_1[int(batsman.split()[-1])-1][1] += outcome
        table_1[int(batsman.split()[-1])-1][2] += 1
        table_1[int(batsman.split()[-1])-1][3] += outcome // 4
        table_1[int(batsman.split()[-1])-1][4] += outcome // 6
    table_2[int(bowler.split()[-1])-1][1] += outcome
    table_2[int(bowler.split()[-1])-1][2] += 0.1
    if outcome == "Out":
        table_2[int(bowler.split()[-1])-1][3] += 1
    table_2[int(bowler.split()[-1])-1][4] = round(table_2[int(bowler.split()[-1])-1][1] / table_2[int(bowler.split()[-1])-1][3], 2)
    
    # If it is the last ball, print out the summary
    if i == len(table_3)-1:
        print("Table 1:\nPlayer name\tRuns\tBalls\t4s\t6s\tOut by")
        for row in table_1:
            print("{}\t{}\t{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

        print("\nTable 2:\nBowler\tRuns\tOvers\tWickets\tAverage")
        for row in table_2:
            print("{}\t{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))

        print("\nTotal Wickets: {}".format(wickets))
