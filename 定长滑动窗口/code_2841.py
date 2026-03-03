from collections import defaultdict
from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        total = 0
        cnt = defaultdict(int)
        current = 0
        for i,num in enumerate(nums):
            current += num
            cnt[num] += 1
            if i < k - 1:
                continue
            if len(cnt) >= m:
                total = max(current, total)
            current -= nums[i-k+1]
            cnt[nums[i-k+1]] -= 1
            if cnt[nums[i-k+1]] == 0:
                del cnt[nums[i-k+1]]
        return total

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    m = 3
    k = 3
    print(Solution().maxSum(nums, m, k))