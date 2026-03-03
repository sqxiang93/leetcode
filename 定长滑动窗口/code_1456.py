class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        alpha = ['a', 'e', 'i', 'o', 'u']
        max_num = 0
        current = 0
        for i, data in enumerate(s):
            if data in alpha:
                current += 1
                max_num = max(max_num, current)
                if max_num == k:
                    break
            if i - k + 1 >= 0 and s[i-k+1] in alpha:
                current -= 1
        return max_num

if __name__ == '__main__':
    s = "abciiidef"
    k = 3
    print(Solution().maxVowels(s, k))