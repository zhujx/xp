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
        return self.subsetsInterative(nums)
    
        
    def subsetsInterative(self, nums):
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
    

    def subsetsRecursive(self, nums):       
        return self.subsetsRecursive(nums, 0)
    

    def subsetsRecursive(self, nums, p):
        if p == len(nums):
            return [[]] # !
     
        subres = self.subsetsRecursive(nums, p+1)

        res = deepcopy(subres)
        
        for s in subres:
            s.append(nums[p])
            
        res.extend(subres)
        
        return res
    

    # 90
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        return self.subsetsWithDupRecursive1(nums, 0)[0]


    def subsetsWithDupRecursive1(self, nums, p):
        if p == len(nums):
            return [[]], 0 # !
     
        subres, latest = self.subsetsWithDupRecursive1(nums, p+1)
        res = deepcopy(subres)

        if p+1 < len(nums) and nums[p+1] != nums[p]: # non-dup
            latest = 0
            
        for s in subres[latest:]:
            s.append(nums[p])
            
        res.extend(subres)
        
        return res, len(subres)


    def subsetsWithDupRecursive2(self, nums):
        nums.sort() # !
        result, results = [], []
        self.subsetsWithDupHelper2(nums, result, results, 0)
        
        return results


    """Decide what to put at the pth position"""
    def subsetsWithDupHelper2(self, nums, result, results, p):
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
