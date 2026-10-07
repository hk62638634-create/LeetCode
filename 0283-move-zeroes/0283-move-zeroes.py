class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
            nums.append(0)