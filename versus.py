import random
#import self as self
import game


def choose():
    with open('players.txt', 'r') as file:
        return random.sample(file, 11)
    pass


class Versus:
    def toss(self):
        self.teams = [self.team_B, self.team_A]
        return random.choice(self.teams)

    def __init__(self):
        self.teams = None
        self.team_A = choose()
        self.team_B = choose()
        self.toss_winner = self.toss()
        self.setter = self.toss_winner
        self.chaser = self.toss_winner - self.teams
        self.onStrike = random.choice(self.setter)
        self.nonStrike = random.choice(self.setter)
        self.bowler = random.choice(self.chaser)
        self.startVersus()

    def _startVersus(self, onstrike, nonstrike, bowler):
        self.onStrike = onstrike
        self.nonStrike = nonstrike
        self.bowler = bowler
        print(self.onStrike, self.nonStrike, self.bowler)
        # self.__init__()
        new_game = game
        new_game.Game.game(self,self.onStrike, self.nonStrike, self.bowler)

    def startVersus(self):
        self.onStrike = self.onStrike
        self.bowler = self.bowler
        self.nonStrike = self.nonStrike
        self._startVersus(self, self.onStrike, self.nonStrike, self.bowler)

        pass
