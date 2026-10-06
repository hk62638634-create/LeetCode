class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            count[ch] = count.get(ch, 0) - 1

        for v in count.values():
            if v != 0:
                return False
        return True
