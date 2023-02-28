import random

# Table 3: Bowler, Batsmen, outcome
table_3 = [[random.choice(["Bowler {}".format(i) for i in range(1, 6)]),
            "Player {}".format(random.randint(1, 11)),
            random.choice(["Out", random.randint(0, 10), random.randint(0, 10)])]
           for i in range(50)]

# Table 2: Bowler, runs, overs, wickets, average
table_2 = [["Bowler {}".format(i), 0, 0, 0, 0] for i in range(1, 6)]

for row in table_3:
    for t2_row in table_2:
        if row[0] == t2_row[0]:
            t2_row[1] += row[2] if type(row[2]) == int else 0
            t2_row[2] += 1
            if type(row[2]) == int:
                t2_row[3] += 1
                t2_row[4] = round(t2_row[1] / t2_row[3], 2)

# Table 1: Player name, Runs, Balls, 4s, 6s, Out by
table_1 = [["Player {}".format(i), 0, 0, 0, 0, ""] for i in range(1, 12)]

for row in table_3:
    for t1_row in table_1:
        if row[1] == t1_row[0]:
            t1_row[1] += row[2] if type(row[2]) == int else 0
            t1_row[2] += 1
            t1_row[3] += 1 if row[2] == 4 else 0
            t1_row[4] += 1 if row[2] == 6 else 0
            if row[2] == "Out":
                t1_row[5] = row[0]

print("Table 1:\nPlayer name\tRuns\tBalls\t4s\t6s\tOut by")
for row in table_1:
    print("{}\t{}\t{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

print("\nTable 2:\nBowler\tRuns\tOvers\tWickets\tAverage")
for row in table_2:
    print("{}\t{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))

print("\nTable 3:\nBowler\tBatsmen\tOutcome")
for row in table_3:
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
