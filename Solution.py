from copy import deepcopy


class Solution(object):

    """
    Combinatorics
    """
    # 78
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 0/1 for choosing
        # incrementally building upon subsets of smaller size
        # alternative method: bit representation
        
        s = [[]]
        for num in nums: 
            tmp = deepcopy(s)
            for elem in tmp:
                elem.append(num)
                s.append(elem)
        
        return s

    # 90
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return self.subsetsWithDupRecursion(nums)

    def subsetsWithDupRecursive(self, nums):
        nums.sort() # !
        result, results = [], []
        self.subsetsWithDupHelper(nums, result, results, 0)
        
        return results

    def subsetsWithDupHelper(self, nums, result, results, p):
        results.append(result[:]) # append one list (i.e., a particular subset)!
        
        for i in range(p, len(nums)):
            if i != p and nums[i] == nums[i-1]: continue # vs i-1
        
            result.append(nums[i])
            self.subsetsWithDupHelper(nums, result, results, i+1)
            result.pop()

    def subsetsWithDupInterative(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort() # sort!
        
        s = [[]]
        lastest = 0 # !
        for i, num in enumerate(nums): 
            
            if i > 0 and nums[i] == nums[i-1]:
                tmp = deepcopy(s[lastest:]) # prevent dups, only adding one more
            else:
                tmp = deepcopy(s)
            
            lastest = len(s)    
            for elem in tmp:
                elem.append(num)
                s.append(elem)
        
        return s
