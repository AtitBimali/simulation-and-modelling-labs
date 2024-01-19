import random


def simulate_dice_game(num_rolls):
    dice_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for _ in range(num_rolls):
        dice_roll = random.randint(1, 6)
        dice_counts[dice_roll] += 1

    print(f"Results for {num_rolls} rolls:")
    for face, count in dice_counts.items():
        print(f"Face {face}: {count} times")


if __name__ == "__main__":
    num_rolls = int(input("Enter the number of rolls: "))
    simulate_dice_game(num_rolls)
