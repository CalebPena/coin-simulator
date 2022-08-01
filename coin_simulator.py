import random

simulations = 10000000

coins = [50, 25, 10, 5, 1]

used = [0]*len(coins)
is_used = [0]*len(coins)
for i in range(simulations):
    value = random.randint(0, 99)
    for i in range(len(coins)):
        n_used, value = divmod(value, coins[i])
        used[i] += n_used
        if n_used:
            is_used[i] += 1

print(used)
print(is_used)
for coin, used in zip(coins, is_used):
    print(str(coin) +': '+ str(used/simulations*100)+'%')