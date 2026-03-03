class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        action = k
        current = 0
        for i,b in enumerate(blocks):
            if b == 'W':
                current += 1
            if i < k - 1:
                continue
            action = min(current, action)
            if action == 0:
                break
            if blocks[i-k+1] == 'W':
                current -= 1
        return action
    
if __name__ == '__main__':
    blocks = "WBBWWBBWBW"
    k = 7
    print(Solution().minimumRecolors(blocks, k))