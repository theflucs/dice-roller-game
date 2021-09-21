import random, operator


def get_number_of_teams():
    try:
        number_of_teams = int(input('How many teams are playing? '))
        return number_of_teams
    except ValueError:
        print('Please type an integer number to continue')
        get_number_of_teams()


def get_number_of_team_members():
    try:
        number_of_team_members = int(input('How many team members in each team? '))
        return number_of_team_members
    except ValueError:
        print('Please type an integer number to continue')
        get_number_of_team_members()


def make_teams(n_teams, n_players):
    team_names = []
    players = []
    teams = []

    for i in range(0, n_teams):
        team = input('Type team name: ')
        team_names.append(team)
        for j in range(0, n_players):
            player = {
                "name": input(f'Type player name of the team {team}: '),
                "team": team,
                "score": 0
            }

            players.append(player)

        teams.append(
            {
                "name": team_names[i],
                "players": players,
                "score": 0
            }
        )
        players = []
    return teams


def init_dice():
    try:
        dice_rolls = int(input('How many dice would you like to roll? '))
        dice_sides = int(input('How many sides are the dice? '))
        dice = {
            "rolls": dice_rolls,
            "sides": dice_sides
        }
        return dice
    except ValueError:
        print('Please type an integer number to continue')
        init_dice()


def init_play(teams):
    rnd = random.randint(0, len(teams) - 1)
    team_start = teams[rnd]

    print('                                         ')
    print(f'{team_start["name"].upper()} starts playing this time!')
    print('                                         ')


def roll_the_dice(dice, player, team):
    rolls = dice['rolls']
    sides = dice['sides']
    dice_sum = 0

    for i in range(0, rolls):
        roll = random.randint(1, rolls)
        dice_sum += roll
        player["score"] = dice_sum

        if roll == 1:
            print(f'{player["name"]}, you rolled a {roll}! Low score!')
        elif roll == sides:
            print(f'{player["name"]}, you rolled a  {roll}! Super score!')
        else:
            print(f'{player["name"]}, you rolled a {roll}!')

    team["score"] += player["score"]

    print(f'{player["name"]} have rolled a total of {dice_sum}')
    print('                                         ')


def make_ranking(teams):
    print('teams: ', teams)
    teams_ranking = sorted(teams, key=lambda i: i['score'], reverse=True)

    print('teams ranking: ', teams_ranking)
    players_ranking = []


def play(dice, teams):
    print('Ok! Everything is set! Good luck!')
    print('                                         ')
    print('                                         ')
    print('------------- START!!!! -------------')
    print('                                         ')

    for i in range(0, len(teams)):
        team = teams[i]
        players = teams[i]["players"]
        players_length = len(players)
        for j in range(0, players_length):
            player = players[j]

            print(f'{player["name"]} press any key and the Enter when you\'re ready to roll!')
            print('Press only Enter to skip your turn!')
            key_pressed = input('')

            if key_pressed:
                print('                                         ')
                print(f'{player["name"]} is rolling the dice.....')
                print('                                         ')
                print('                                         ')
                roll_the_dice(dice, player, team)


def main():
    number_of_teams = get_number_of_teams()
    number_of_team_members = get_number_of_team_members()
    teams = make_teams(number_of_teams, number_of_team_members)
    init_play(teams)
    dice = init_dice()
    play(dice, teams)
    make_ranking(teams)


# the function main will run whenever you run the Python script.
if __name__ == "__main__":
    main()
