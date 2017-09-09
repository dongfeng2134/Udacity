import random as rd

def simulate_coin_flips(num_trials):
    heads = 0
    tails = 0
    p_heads = 0.5
    for i in range(num_trials):
        random_number = rd.random()
        if random_number < p_heads:
            heads = heads + 1
        else:
            tails += 1
    percent_heads = heads / num_trials
    return percent_heads
    
percentage = simulate_coin_flips(200) # calling the function
print(percentage)


print(simulate_coin_flips(100))
print(simulate_coin_flips(10000))
print(simulate_coin_flips(1000000))
