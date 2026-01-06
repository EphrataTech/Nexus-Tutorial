class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = len(nums1)-1
        j = len(nums2)-1

        if nums1[j] < nums[j]:
            nums1[i] = nums[j]
            i -= 1
            j -= 1

            



       
     
