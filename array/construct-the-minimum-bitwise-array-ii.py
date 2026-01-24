class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue
            
            for i in range(1, 32):
                if not (n & (1 << i)):
                    res = n ^ (1 << (i - 1))
                    ans.append(res)
                    break
        return ans