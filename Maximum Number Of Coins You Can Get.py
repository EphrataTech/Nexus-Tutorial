class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count  = 0
        j = len(piles) // 3
        k = 1
        piles.sort(reverse = True)
        

        # while k < len(piles):
        for i in range(j):
            count += piles[k]
            k += 2

        return count
               
            

            

        

