from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        current = 0
        avgs = [-1]*len(nums)
        for i, num in enumerate(nums):
            current += num
            if i < 2*k:
                continue
            avgs[i-k] = current // (2*k + 1)
            current -= nums[i-2*k]
        return avgs

if __name__ == '__main__':
    nums = [7,4,3,9,1,8,5,2,6]
    k = 3
    print(Solution().getAverages(nums, k))