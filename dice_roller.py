import random


def main():
    first = 1
    last = 6
    dice_rolls = 2
    dice_sum = 0

    for i in range(0, dice_rolls):
        roll = random.randint(first, last)
        dice_sum += roll

    print(f'You rolled a total of {dice_sum}')


# the function main will run whenever you run the Python script.
if __name__ == "__main__":
    main()
