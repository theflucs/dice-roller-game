import random


def main():
    first = 1
    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))
    dice_sum = 0

    for i in range(0, dice_rolls):
        roll = random.randint(first, dice_rolls)
        dice_sum += roll

        if roll == 1:
            print(f'You rolled a total of {roll}! Critical fail!')
        elif roll == dice_size:
            print(f'You rolled a total of {roll}! Critical success!')
        else:
            print(f'You rolled a total of {roll}!')

    print(f'You have rolled a total of {dice_sum}')


# the function main will run whenever you run the Python script.
if __name__ == "__main__":
    main()
