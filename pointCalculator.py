# The objective of this script is to sum up the fantasy points for a given week
# Will take an input for a week, and will use standard ESPN PPR Scoring


from sportsreference.nfl.boxscore import Boxscores, Boxscore, BoxscorePlayer, AbstractPlayer

# gather the boxscores for a certain week and year
# will eventually be taken as input

class OutputPlayer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.points = 0

#takes in a Player and returns an OutputPlayer
def calcPoints(player):
    #error, use roster for player positions
    test = OutputPlayer(player.name, player.position)
    return test


games = Boxscores(16, 2020)

p1 = OutputPlayer("Nathan Wales", "WR")
print(p1.name + ": " + p1.position + " points = " + str(p1.points))

games_dic = games.games
for game in games_dic['16-2020']:
    curr_game = Boxscore(game['boxscore'])
    home_players = curr_game.home_players
    for player in home_players:
        test = calcPoints(player)
        print(test.name + "\n")
    
    #away_players = curr_game.away_players
    #for player in away_players: