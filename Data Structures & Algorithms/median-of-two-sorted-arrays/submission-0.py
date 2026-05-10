class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        merged = merged + nums1[i:] + nums2[j:]
        
        middle = len(merged) // 2
        
        if len(merged) % 2 == 1:
            return merged[middle]
        else:
            return (merged[middle] + merged[middle - 1]) / 2