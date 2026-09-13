from collections import Counter

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:

        ones1 = [(r, c) for r, row in enumerate(img1) for c, val in enumerate(row) if val == 1]
        ones2 = [(r, c) for r, row in enumerate(img2) for c, val in enumerate(row) if val == 1]
        offset_counts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                offset = (r1 - r2, c1 - c2)
                offset_counts[offset] += 1
        return max(offset_counts.values()) if offset_counts else 0
