class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)

        # Sort to use two pointers and skip duplicates
        nums.sort()

        for i in range(n):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                # Skip duplicate second elements
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                # Find the remaining two elements using two pointers
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total == target:
                        # Found a valid quadruplet
                        ans.append([
                            nums[i], nums[j], nums[k], nums[l]
                        ])

                        k += 1
                        l -= 1

                        # Skip duplicate third elements
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1

                        # Skip duplicate fourth elements
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

                    elif total < target:
                        # Need a larger sum
                        k += 1

                    else:
                        # Need a smaller sum
                        l -= 1

        return ans