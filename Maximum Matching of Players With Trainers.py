class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i = len(players) - 1
        j = len(trainers) - 1
        count = 0
        players.sort()
        trainers.sort()

        while i >=0 and j >=0:
            if trainers[j] >= players[i]:
                count += 1
                i -= 1
                j -= 1

            else:

                i -= 1
                
                

        return count


        
