
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Create a list of player tuples, combining scores and ages
        players = list(zip(ages, scores))
        
        # Sort the players based on ages and then scores (in descending order)
        players.sort()
        
        # Initialize a list to store the maximum team score for each player
        dp = [0] * len(players)
        
        # Initialize the maximum team score with the score of the first player
        ans = players[0][1]
        
        # Loop through the players
        for i in range(len(players)):
            # Initialize the current player's score
            dp[i] = players[i][1]
            
            # Compare the current player's score with other players with lower ages
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])
            
            # Update the maximum team score
            ans = max(ans, dp[i])
        
        return ans
