class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = m + n
        if n != 0:
            for i in range(temp):
                if m == 0 :
                    nums1[temp-1-i] = nums2[n-1]
                    n -= 1
                    continue
                else:
                    if nums1[m-1] >= nums2[n-1]:
                        nums1[temp-1-i] = nums1[m-1]
                        m -= 1
                    else:
                        nums1[temp-1-i] = nums2[n-1]
                        n -= 1
                    if n == 0:
                        break
