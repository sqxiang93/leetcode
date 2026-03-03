from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        num = 0
        current = 0
        for i, n in enumerate(arr):
            current += n
            if i < k - 1:
                continue
            if current / k >= threshold:
                num += 1
            current -= arr[i-k+1]
        return num

if __name__ == '__main__':
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    print(Solution().numOfSubarrays(arr, k, threshold))