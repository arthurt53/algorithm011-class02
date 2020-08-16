class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        in_arr2 = []
        not_in_arr2 = []
        Hash = {}
        for i in arr1:
            Hash[i] = Hash.get(i, 0) + 1
        arr1 = set(arr1)
        for j in arr1:
            if j not in arr2:
                not_in_arr2 += [j]*Hash[j]
        not_in_arr2.sort()
        for k in arr2:
            in_arr2 += [k]*Hash[k]
        return in_arr2+not_in_arr2
