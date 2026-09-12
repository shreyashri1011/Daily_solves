from bisect import bisect_left
from typing import List

class Solution(object):
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store as (right, left, weight, original_index)
        arr = sorted([(intervals[i][1], intervals[i][0], intervals[i][2], i) for i in range(n)])
        
        # Binary search helper array containing just right-endpoints
        rights = [x[0] for x in arr]

        # dp[i][j] stores the best (weight, tuple_of_indices) using a subset of first i intervals taking j intervals
        # We store negative indices or compare tuple-wise to enforce lexicographical ordering naturally
        # Structure: dp[j] for current prefix iteration to save memory
        dp = [[(0, ())] * 5 for _ in range(n + 1)]

        for i in range(n):
            r, l, weight, idx = arr[i]
            
            # Find the largest index k where arr[k][0] < l
            k = bisect_left(rights, l, hi=i)

            for j in range(1, 5):
                # Choice 1: Do not pick interval i
                best_without = dp[i][j]

                # Choice 2: Pick interval i
                prev_weight, prev_indices = dp[k][j - 1]
                new_weight = prev_weight + weight
                # Maintain sorted order of indices for tie-breaking
                new_indices = tuple(sorted(prev_indices + (idx,)))
                best_with = (new_weight, new_indices)

                # Determine the better choice:
                # 1. Higher weight wins
                # 2. On tie, lexicographically smaller index list wins
                if best_with[0] > best_without[0]:
                    dp[i + 1][j] = best_with
                elif best_with[0] < best_without[0]:
                    dp[i + 1][j] = best_without
                else:
                    # Weights are equal: pick the smaller index list
                    if best_with[1] < best_without[1]:
                        dp[i + 1][j] = best_with
                    else:
                        dp[i + 1][j] = best_without

        return list(dp[n][4][1])