import random

# Table 1: Player name, Runs, Balls, 4s, 6s, Out by
table_1 = [["Player {}".format(i), random.randint(0, 150), random.randint(0, 150), random.randint(0, 20), random.randint(0, 10), "Bowler {}".format(random.randint(1, 5))] for i in range(1, 12)]

print("Table 1:\nPlayer name\tRuns\tBalls\t4s\t6s\tOut by")
for row in table_1:
    print("{}\t{}\t{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

# Table 2: Bowler, runs, overs, wickets, average
table_2 = [["Bowler {}".format(i), random.randint(0, 100), random.randint(0, 10), random.randint(0, 5), round(random.uniform(10, 50), 2)] for i in range(1, 6)]

print("\nTable 2:\nBowler\tRuns\tOvers\tWickets\tAverage")
for row in table_2:
    print("{}\t{}\t{}\t{}\t{}".format(row[0], row[1], row[2], row[3], row[4]))

# Table 3: Bowler, Batsmen, outcome
table_3 = [[random.choice(table_2)[0], "Player {}".format(random.randint(1, 11)), random.choice(["Out", random.randint(0, 10), random.randint(0, 10)])] for i in range(50)]

print("\nTable 3:\nBowler\tBatsmen\tOutcome")
for row in table_3:
    print("{}\t{}\t{}".format(row[0], row[1], row[2]))
