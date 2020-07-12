class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()
        def backtrack(nums, tmp):
            if len(nums) == len(tmp):
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i in visited or (i > 0 and i - 1 not in visited and nums[i-1] == nums[i]):
                    continue
                visited.add(i)
                backtrack(nums, tmp + [nums[i]])
                visited.remove(i)
        backtrack(nums, [])
        return res
