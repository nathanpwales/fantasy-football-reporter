# The objective of this script is to sum up the fantasy points for a given week
# Will take an input for a week, and will use standard ESPN PPR Scoring


from sportsreference.nfl.boxscore import Boxscores, Boxscore, BoxscorePlayer, AbstractPlayer
from sportsreference.nfl.roster import Player
import sqlite3

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
    #if curr('2020') is not None:
       # if curr('2020').position is not None:
    try:
        test = OutputPlayer(player.name, str(curr('2020').position).upper())
    except:
        return None 
       # else :
           # return None
    #else :
      #  return None
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

    test.points = round(test.points, 2)
    
    #print(testString)
    return test

def insertOutputPlayer(out_player):
    c.execute("INSERT INTO players VAlUES (:name, :position, :points)", 
    (out_player.name, out_player.position, out_player.points))

games = Boxscores(16, 2020)
conn = sqlite3.connect('playerPointDatabase2020.db')
c = conn.cursor()

c.execute("DELETE FROM players")



games_dic = games.games
for game in games_dic['16-2020']:
    curr_game = Boxscore(game['boxscore'])
    home_players = curr_game.home_players
    for player in home_players:
        test = calcPoints(player)
        if test is not None:
            if test.points != 0.0:
                insertOutputPlayer(test)
                print(test.name + " " + str(test.position) + ": " + str(test.points) + "\n")
    
    away_players = curr_game.away_players
    for player in away_players: 
        test = calcPoints(player)
        if test is not None:
            if test.points != 0.0:
                insertOutputPlayer(test)
        #    print(test.name + " " + str(test.position) + ": " + str(test.points) + "\n")

conn.commit()
conn.close()
