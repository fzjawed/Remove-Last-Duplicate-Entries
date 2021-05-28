class Solution:
    def solve(self, nums):
        c = Counter(nums)
        res = []
        for val in nums:
            if c[val] == 0:
                continue
            else:
                res.append(val)
                c[val] -= 1
            if c[val] == 1:
                c[val] = 0

        return res