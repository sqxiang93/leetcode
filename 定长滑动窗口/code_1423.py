from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = s = sum(cardPoints[:k])
        for i in range(1, k+1):
            s += cardPoints[-i] - cardPoints[k - i]
            ans = max(ans, s)
        return ans

if __name__ == '__main__':
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    print(Solution().maxScore(cardPoints, k))