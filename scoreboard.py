class ScoreBoard:

    def __init__(self, team_a, team_b):
        self.team_A = team_a
        self.team_B = team_b
        pass

    def current_batsmen(self, onstrike, nonstrike):
        if self.onstrike == onstrike:
            pass
        else:
            pass

    def update_score(self, update):
        outornot, run, onstrike, nonstrike, bowler = update
        self.batsman_run += run
        self.bowler_wicket += 0 if outornot == "out" else 1
