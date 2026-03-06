from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = cnt0 = left = 0
        for right, x in enumerate(nums):
            cnt0 += 1 - x
            while cnt0 > 1:
                cnt0 -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left)
        return ans

if __name__ == "__main__":
    nums = [1, 1, 0, 1]
    print(Solution().longestSubarray(nums))