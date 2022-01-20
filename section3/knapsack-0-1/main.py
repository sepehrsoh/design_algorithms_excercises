def knapsack(W, wt, val):
    n = len(val)
    dp = [0 for _ in range(W + 1)]

    for i in range(1, n + 1):
        for w in range(W, 0, -1):
            if wt[i - 1] <= w:
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])
    return dp[W]


if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    Total_weight = 50
    print(knapsack(Total_weight, weights, values))
