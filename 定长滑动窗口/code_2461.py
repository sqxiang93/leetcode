from ast import List
from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        p = defaultdict()
        total = 0
        current = 0
        for i, num in enumerate(nums):
            if num not in p:
                p[num] = 0
            p[num] += 1
            current += num
            if i < k-1:
                continue
            if len(p) == k:
                total = max(current, total)
            p[nums[i-k+1]] -= 1
            if p[nums[i-k+1]] == 0:
                del p[nums[i-k+1]]
            current -= nums[i-k+1]
        return total

if __name__ == '__main__':
    nums = [1,5,4,2,9,9,9]
    k = 3
    print(Solution().maximumSubarraySum(nums, k))