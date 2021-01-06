# The objective of this script is to sum up the fantasy points for a given week
# Will take an input for a week, and will use standard ESPN PPR Scoring


from sportsreference.nfl.boxscore import Boxscores, Boxscore, BoxscorePlayer, AbstractPlayer
from sportsreference.nfl.roster import Player

# gather the boxscores for a certain week and year
# will eventually be taken as input

class OutputPlayer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.points = 0

#takes in a BoxscorePlayer and returns an OutputPlayer
def calcPoints(player):
    curr = Player(player.player_id)
    test = OutputPlayer(player.name, str(curr('2020').position).upper())
    testString = ""

    result = player.receiving_yards
    if result is not None:
        test.points += ((float(result)) * .1)
    testString += str(result) + " "
    
    result = player.rush_yards
    if result is not None:
        test.points += ((float(result)) * .1)
    testString += str(result) + " "
    
    result = player.rush_touchdowns
    if result is not None:
        test.points += ((float(result)) * 6)
    testString += str(result) + " "

    result = player.receiving_touchdowns
    if result is not None:
        test.points += ((float(result)) * 6)
    testString += str(result) + " "

    result = player.passing_touchdowns
    if result is not None:
        test.points += ((float(result)) * 4)
    testString += str(result) + " "

    result = player.passing_yards
    if result is not None:
        test.points += ((float(result)) * .04)
    testString += str(result) + " "

    result = player.receptions
    if result is not None:
        test.points += ((float(result)) * 1)
    testString += str(result) + " "

    result = player.fumbles_lost
    if result is not None:
        test.points += ((float(result)) * -2)
    testString += str(result) + " "

    result = player.interceptions_thrown
    if result is not None:
        test.points += ((float(result)) * -2)
    testString += str(result) + " "

    result = player.punt_return_touchdown
    if result is not None:
        test.points += ((float(result)) * 6)
    testString += str(result) + " "

    result = player.kickoff_return_touchdown
    if result is not None:
        test.points += ((float(result)) * 6)
    testString += str(result) + " "
    
    #for some reaason this returns the fumble recovery yards
    #api is broken, this currently gives the wrong data, but should
    #work once sports reference has been updated =
    result = player.fumbles_recovered_for_touchdown
    if result is not None:
        test.points += ((float(result)) * 6)
    testString += str(result) + " "

    result = player.extra_points_made
    if result is not None:
        test.points += ((float(result)) * 1)
    testString += str(result) + " "

    result = player.field_goals_made
    if result is not None:
        test.points += ((float(result)) * 3)
    testString += str(result) + " "

    result = player.field_goals_attempted
    if result is not None:
        made = player.field_goals_made
        if made is not None:
            test.points += ((float(result-made)) * -1)
    testString += str(result) + " "

    #Points missing
    # 2 point conversion (passing, receiving, rushing)
    # differnet points for field goals

    

    test.points = round(test.points, 2)
    
    #print(testString)
    return test


games = Boxscores(16, 2020)

games_dic = games.games
for game in games_dic['16-2020']:
    curr_game = Boxscore(game['boxscore'])
    home_players = curr_game.home_players
    for player in home_players:
        test = calcPoints(player)
        if test.points != 0.0:
            print(test.name + " " + str(test.position) + ": " + str(test.points) + "\n")
    
    away_players = curr_game.away_players
    for player in away_players:
        test = calcPoints(player)
        if test.points != 0.0:
            print(test.name + " " + str(test.position) + ": " + str(test.points) + "\n")