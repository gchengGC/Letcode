class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        while i < len(nums):
            if (target - nums[i]) in nums:
                for j in range(len(nums)):
                    if nums[j] == (target - nums[i]) and j > i :
                        return [i,j]
            i = i + 1

    def twoSum1(self, nums, target):
        i = 0
        n = len(nums)
        while i < n :
            j = i
            while j < n:
                if (nums[i] + nums[j] == target):
                    return [i,j]
                else:
                    continue
                j = j + 1

    def twoSum3(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []
if __name__ == '__main__':
    a = Solution()
    nums = [1,1,4,5,6,7,14]
    target = 5
    print(a.twoSum3(nums,target))