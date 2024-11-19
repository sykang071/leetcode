# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
#
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

test1 = [0,1,2,2,3,0,4,2]
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

    #    Solution 1:
    #     k = 0
    #     # remove value from list that is equal to val
    #     for idx, num in enumerate(nums):
    #         if num != val:
    #             nums[k] = num
    #             k +=1
    #
    #     return k

    #Solution 2 (best)
    while val in nums:
        nums.remove(val)

if __name__ == '__main__':
    s = Solution()
    s.removeElement(test1, 2)
