class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_lens = [float('inf')] * n
        ans = float('inf')
        window_sum = 0
        left = 0
        for right in range(n):
            window_sum += arr[right]
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
            if window_sum == target:
                curr_len = right - left + 1
                if left > 0 and min_lens[left - 1] != float('inf'):
                    ans = min(ans, min_lens[left - 1] + curr_len)
                min_lens[right] = curr_len
            if right > 0:
                min_lens[right] = min(min_lens[right], min_lens[right - 1])
                
        return ans if ans != float('inf') else -1
