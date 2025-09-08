class LCSClass:
    """...write comment for this class..."""
     #This class finds the Longest Common Subsequence (LCS) 
     #between two strings using Dynamic Programming.

    def __init__(self):
        """...write comment about this method...
        """
        #This creates an LCSClass instance
        pass

    
    def find(self, x, y):
        """
        Here we find the LCS length for strings x and y.
        """

        # If either string is empty, the LCS is 0
        if not x or not y:
            return 0

        n = len(x)
        m = len(y)

        # Create a table with all 0s
        # dp[i][j] will hold the LCS length of x[:i] and y[:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Then we go through each character in both strings
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if x[i - 1] == y[j - 1]:
                    # If characters match, add 1 to the diagonal value
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # If not, take the bigger value from top or left
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The answer is in the bottom-right cell
        return dp[n][m]