class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                # nums[j] = 0
                i += 1

        for k in range(i, len(nums)):
            nums[k] = 0
        
        
      
        
