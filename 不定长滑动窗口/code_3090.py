from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cns = defaultdict(int)
        total = 0
        left = 0
        for right, c in enumerate(s):
            cns[c] += 1
            while cns[c] > 2:
                cns[s[left]] -= 1
                left += 1
            total = max(total, right - left + 1)
        return total

if __name__ == "__main__":
    s = "abcabc"
    print(Solution().maximumLengthSubstring(s))