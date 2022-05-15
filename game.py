from random import choice

NO_OF_OVERS = 5
BALL_PER_OVER = 6
ON_STRIKE = None
NON_STRIKE = None
CURRENT_BOWLER = None
OUTCOMES = [{'0': 0}, {'1': 1}, {'2': 2}, {'3': 3}, {'4': 4}, {'5': 5}, {'6': 6},
            {'0NB': 1}, {'1NB': 2}, {'2NB': 3}, {'4NB': 5}, {'6NB': 7},
            {'0WD': 1}, {'1WD': 2}, {'2WD': 3}, {'4WD': 5},
            {'1LB': 1}, {'2LB': 2}, {'4LB': 4},
            {'1B': 1}, {'2B': 2}, {'3B': 3}, {'4B': 4},
            {'Bowled': 0}, {'Caught': 0}, {'LBW': 0},
            {'1RNT': 0}, {'2RNT': 1}]


def check_if_out(outcome_from_event):
    key, value = outcome_from_event
    if key == 'Bowled' or key == 'Caught' or key == 'LBW' or key == '1RNT' or key == '2RNT':
        return True
    pass


class Game:
    def __init__(self, team_a, team_b):
        self.processed_result = None
        self.result_per_ball = None
        self.fair_ball = None
        self.ball = None
        self.over = None
        self.this_outcome = None
        self.outcome = None
        self.currentBowler = None
        self.team_A = team_a
        self.team_B = team_b
        self.onStrike = ON_STRIKE
        self.nonStrike = NON_STRIKE

    def outcome(self):
        global OUTCOMES
        self.result_per_ball = choice(OUTCOMES)
        # print(self.outcome)
        return self.result_per_ball
        pass

    def isFair(self):
        key = self.result_per_ball
        key = str(key.keys())
        # print('printing in is-fair', type(key))
        if key.endswith("NB") or key.endswith("WD"):
            return False
        else:
            return True

    def new_ball_event(self, on_strike, non_strike, current_bowler):
        self.onStrike = on_strike
        self.nonStrike = non_strike
        self.currentBowler = current_bowler
        self.this_outcome = Game.outcome(self)
        print(self.this_outcome)
        return self.this_outcome

    def process(self, result_per_ball, non_strike=None, on_strike=None):
        print(self.outcome)
        if result_per_ball is not check_if_out(self.outcome):
            key, value = self.outcome
            if value % 2 != 0:
                self.onStrike = non_strike
                self.nonStrike = on_strike
            return 'not-out', value, self.onStrike, self.nonStrike, self.currentBowler
        else:
            key, value = self.outcome
            if key == '2RNT':
                self.onStrike = non_strike
                self.nonStrike = on_strike
            return 'out', value, self.onStrike, self.nonStrike, self.currentBowler
        pass

    def game(self, onStrike, nonStrike, bowler):
        self.onStrike = onStrike
        self.nonStrike = nonStrike
        self.currentBowler = bowler
        self.over = 0
        self.ball = 0
        self.fair_ball = 0
        print(self.over)

        while self.over < NO_OF_OVERS:
            self.result_per_ball = Game.new_ball_event(self, self.onStrike, self.nonStrike, self.currentBowler)
            print('i am here with', self.over, self.fair_ball, self.result_per_ball)
            if self.fair_ball == 6:
                self.over += 1
                self.fair_ball = 0
                continue
            else:
                if Game.isFair(self):
                    self.fair_ball += 1
                    # self.processed_result = Game.process(self.result_per_ball)

        pass

    pass
