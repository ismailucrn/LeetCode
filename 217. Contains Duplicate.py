class Solution(object):
    def containsDuplicate(self, nums):
        lst = set()
        for i in nums:
            if i in lst:
                return True
            lst.add(i)
        return False