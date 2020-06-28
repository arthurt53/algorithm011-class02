class Solution_1:
    #切片法
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = len(nums) - (k - int(k / len(nums)) * len(nums))
        nums[:] = nums[temp:] + nums[:temp]


class Solution_2:
    #三次反转法
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def swap(a, b):
            while a < b:
                nums[a] , nums[b] = nums[b] , nums[a]
                a += 1
                b -= 1
        swap(0 , len(nums) - k - 1)
        swap(len(nums) - k , len(nums) - 1)
        swap(0 , len(nums) - 1)
