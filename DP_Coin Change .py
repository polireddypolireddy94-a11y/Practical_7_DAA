def make_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] > amount:
        return -1

    return dp[amount]

coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter the amount: "))

result = make_change(coins, amount)

if result == -1:
    print("Change cannot be made")
else:
    print("Minimum number of coins:", result)
