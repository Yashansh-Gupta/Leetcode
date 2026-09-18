class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
        def check_valid_substring(start_idx):
            end_idx = last[s[start_idx]]
            curr_idx = start_idx
            
            while curr_idx <= end_idx:
                char = s[curr_idx]
                if first[char] < start_idx:
                    return -1
                end_idx = max(end_idx, last[char])
                curr_idx += 1
            return end_idx
        valid_intervals = []
        for char in first:
            start = first[char]
            end = check_valid_substring(start)
            if end != -1:
                valid_intervals.append((start, end))
        valid_intervals.sort(key=lambda x: x[1])
        ans = []
        last_end = -1
        for start, end in valid_intervals:
            if start > last_end:
                ans.append(s[start : end + 1])
                last_end = end
                
        return ans
