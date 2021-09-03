import random


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
    all_players = []
    teams = []

    for i in range(0, n_teams):
        team = input('Type team name: ')
        team_names.append(team)
        for j in range(0, n_players):
            player = input(f'Type player name of the team {team}: ')
            all_players.append(player)
        teams.append(
            {
                "name": team_names[i],
                "players": all_players
            }
        )
        all_players = []
    return teams


def init_play(teams):
    rnd = random.randint(0, len(teams) - 1)
    team_start = teams[rnd]

    print('                                         ')
    print(f'{team_start["name"].upper()} starts playing this time!')
    print('                                         ')


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

def roll_the_dice(dice, player, team):
    rolls = dice['rolls']
    sides = dice['sides']
    dice_sum = 0

    for i in range(0, rolls):
        roll = random.randint(1, rolls)
        dice_sum += roll

        if roll == 1:
            print(f'You rolled a {roll}! Low score!')
        elif roll == sides:
            print(f'You rolled a  {roll}! Super score!')
        else:
            print(f'You rolled a {roll}!')

    print('                                         ')
    print(f'{player} have rolled a total of {dice_sum}')
    print('                                         ')


def play(dice, teams):
    print('Ok! Everything is set! Good luck!')
    print('                                         ')
    print('                                         ')
    print('------------- START!!!! -------------')
    print('                                         ')

    for i in range(0, len(teams)):
        team = teams[i]["name"]
        players = teams[i]["players"]
        for j in range(0, len(players)):
            player = players[j]

            print(f'{player} press any key and the Enter when you\'re ready to roll!')
            key_pressed = input('')

            if key_pressed:
                print('                                         ')
                print(f'{player} is rolling the dice.....')
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


# the function main will run whenever you run the Python script.
if __name__ == "__main__":
    main()
