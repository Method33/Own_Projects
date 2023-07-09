import random

def monty_hall_game(switch_doors, num_trials=10000):
    winning_count = 0
    for _ in range(num_trials):
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)

        # player's initial choice
        initial_choice = random.choice([0, 1, 2])

        # Monty opens a door
        remaining_doors = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        door_to_open = random.choice(remaining_doors)

        # Does player switch?
        if switch_doors:
            final_choice = [i for i in range(3) if i != initial_choice and i != door_to_open][0]
        else:
            final_choice = initial_choice

        if doors[final_choice] == 'car':
            winning_count += 1

    return winning_count / num_trials

print("Probability of winning if you do NOT switch: ", monty_hall_game(switch_doors=False))
print("Probability of winning if you DO switch: ", monty_hall_game(switch_doors=True))
