import re
import collections
import pprint

red_gex = r'(\d red)'
blue_gex = r'(\d blue)'
green_gex = r'(\d green)'
with open('input.txt') as f:
    games = [x.strip().split(':') for x in f.readlines()]

def splitSubGames(game):
    return game.split(';')

def splitColors(color, game: [str, str]):
    sub_games = splitSubGames(game[1])

    color_counts = [re.findall('(\d+) '+color, sg) for sg in sub_games]

    color_counts = [(0 if not x else int(x[0])) for x in color_counts]

    return color_counts

def buildDict(games):
    colors = ['red', 'blue', 'green']

    game_color_count = {}

    for game in games:
        game_color_count[game[0]] = {}
        for color in colors:
            game_color_count[game[0]][color] = splitColors(color, game)

    return game_color_count

def isValidColor(color_counts, test):
    for count in color_counts:
        if count > test: return True
    return False

def isValidSubGame(sub_game, tests):
    red,green,blue = sub_game
    red_test,green_test,blue_test = tests
    
    red_pass = int(red) <= red_test
    green_pass = int(green) <= green_test
    blue_pass = int(blue) <= blue_test

    return (red_pass and green_pass and blue_pass)

def findLargest(reds, blues, greens):
    return [max(reds), max(blues), max(greens)]

def isValidGame(game, tests, part_two=True):

    game_pass = True

    if part_two:
        colors = (game['red'], game['green'], game['blue'])
        largest = findLargest(*colors)
        print(largest)
        return largest


    else:
        for i in range(len(game['red'])):
            sub_game = (game['red'][i], game['green'][i], game['blue'][i])
            sub_game_pass = isValidSubGame(sub_game,tests)
    #        print(sub_game_pass)
    #        print(' ',end='')
    #        print(sub_game, sub_game_pass)
            game_pass = (game_pass and sub_game_pass)

    return game_pass



def solvePartOne(games, part_two=True):
    games_dict = buildDict(games)

    tests = [12,13,14]
    games_pass_list = []

    
    for i,game in enumerate(games_dict.values()):
        print(game)
        game_pass = isValidGame(game, tests, part_two)
        games_pass_list.append(game_pass)

    sum = 0
    if not part_two:
        for i,g in enumerate(games_pass_list):
            if g: sum += i+1
    #        print(i,g)
        
        print('part 1')
        print(sum)

    else:
        from math import prod
        print(len(games_pass_list))
        for trio in games_pass_list:
            power = prod(trio)
            sum+=power
    


        print('part 2')
        print(sum)
    
solvePartOne(games, part_two=True)
