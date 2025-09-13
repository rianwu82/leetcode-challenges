class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] = counter[num] + 1
                return True
            elif num not in counter:
                counter[num] = 1
        return False        