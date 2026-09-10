class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []

        i = 0
        j = 0

        # Compare elements from both arrays
        while i < len(nums1) and j < len(nums2):

            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Add remaining elements from nums1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        # Add remaining elements from nums2
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        # Find median
        n = len(merged)

        if n % 2 == 1:
            # Odd number of elements
            return float(merged[n // 2])

        else:
            # Even number of elements
            middle1 = merged[n // 2 - 1]
            middle2 = merged[n // 2]

            return (middle1 + middle2) / 2.0