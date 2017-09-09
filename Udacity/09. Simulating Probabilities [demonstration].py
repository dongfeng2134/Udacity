import random as rd
from matplotlib import pyplot as plt

def simulate_dice_rolls(N):
    roll_counts = [0,0,0,0,0,0]
    for i in range(N):
        roll = rd.choice([1,2,3,4,5,6])
        index = roll - 1
        roll_counts[index] = roll_counts[index] + 1
    return roll_counts

def show_roll_data(roll_counts):
    number_of_sides_on_die = len(roll_counts)
    for i in range(number_of_sides_on_die):
        number_of_rolls = roll_counts[i]
        number_on_die = i+1
        print(number_on_die, "came up", number_of_rolls, "times")
        
roll_data = simulate_dice_rolls(1000)
show_roll_data(roll_data)

def visualize_one_die(roll_data):
    roll_outcomes = [1,2,3,4,5,6]
    fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.bar(roll_outcomes, roll_data)
    ax1.set_xlabel("Value on Die")
    ax1.set_ylabel("# rolls")
    ax1.set_title("Simulated Counts of Rolls")

    ax2.bar(roll_outcomes, roll_data)
    ax2.set_xlabel("Value on Die")
    ax2.set_ylabel("# rolls")
    ax2.set_title("Simulated Counts of Rolls")
    plt.show()

roll_data = simulate_dice_rolls(500)
visualize_one_die(roll_data)
