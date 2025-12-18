class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new = sorted(nums)
        n = len(new)
        newArr= []

        for i in range(n):
            if new[i] == target:
                newArr.append(i)
        return newArr
        
