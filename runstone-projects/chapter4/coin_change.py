def make_change_1(coin_denoms, change):
    if change in coin_denoms:
        return 1
    min_coins = float("inf")
    for i in [c for c in coin_denoms if c <= change]:
        num_coins = 1 + make_change_1(coin_denoms, change - i)
        min_coins = min(num_coins, min_coins)
    return min_coins

# print(make_change_1([1,5,10,25], 63))  extremely inefficient solution

def make_change_2(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + make_change_2(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
            known_results[change] = min_coins   
    print(known_results)
    return min_coins


print(make_change_2([1, 5, 10, 25], 63, [0] * 64))

# Dynamic concepts
def make_change_3(coin_value_list, change, min_coins):
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_counts:
                coin_count = min_coins[cents - j] + 1
            min_coins[cents] = coin_count
    return min_coins[change]