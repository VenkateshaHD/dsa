def min_cost_path(grid):
    if not grid or not grid[0]:
        return 0

    m = len(grid)
    n = len(grid[0])

    # Initialize DP table
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Base case: starting cell
    dp[0][0] = grid[0][0]

    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

# --- Custom Input ---

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
print("Enter grid row by row (space-separated):")

grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

result = min_cost_path(grid)
print("Minimum cost to reach bottom-right:", result)
