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
        return self.subsetsIterExpansion(nums)

    """ Iteratively build upon subsets of smaller size: O(2^n) """ 
    def subsetsIterExpansion(self, nums):             
        s = [[]]
        for num in nums: # adding one more each time
            tmp = deepcopy(s)
            for elem in tmp:
                elem.append(num)
                s.append(elem)              
        return s
    

    """ Convert from bit representation: O(n.2^n)"""
    def subsetsIterBitRepresentation(self, nums):
        s = []
        length = len(nums)
        for i in range(1 << length):
            result = []
            b = 1
            for j in range(length):
                if b && i != 0: result.append(nums[j])
                b = b << 1;
            s.append(deepcopy(result))
        return s


    """ [Backward] Recursively build upon subsets of smaller size: O(2^n) """
    def subsetsRecursiveSuffix(self, nums):       
        return self.subsetsRecursiveSuffixHelper(nums, 0)
    
    def subsetsRecursiveSuffixHelper(self, nums, p):
        if p == len(nums): return [[]] # !     
        subres = self.subsetsRecursiveSuffixHelper(nums, p+1)
        res = deepcopy(subres)
        for s in subres:
            s.append(nums[p])          
            res.append(s)      
        return res


    """ [Forward] Recursively build upon subsets of smaller size: O(2^n + n^2) = O(2^n) """
    def subsetsRecursivePrefix(self, nums):       
        result, results = [], [[]] # !
        self.subsetsRecursivePrefixHelper(nums, result, results, 0)     
        return results

    def subsetsRecursivePrefixHelper(self, nums, result, results, p):       
        for i in range(p, len(nums)): # decide what to put at pth position        
            result.append(nums[i])
            results.append(deepcopy(result))
            self.subsetsRecursivePrefixHelper(nums, result, results, i+1)
            result.pop()


    # 90
    def subsetsWithDup(self, nums):
        #return self.subsetsWithDupIterExpansion(nums)
        return self.subsetsWithDupRecursiveSuffix(nums)

    
    """ Iteratively build upon subsets of smaller size: O(2^n) """ 
    def subsetsWithDupIterExpansion(self, nums): 
        nums.sort() # sort!       
        s = [[]]
        lastest = 0 # !
        for i, num in enumerate(nums):            
            if i > 0 and nums[i] == nums[i-1]:
                tmp = deepcopy(s[lastest:]) # only extending for the largest subsets
            else:
                tmp = deepcopy(s)
                
            lastest = len(s)    
            for elem in tmp:
                elem.append(num)
                s.append(elem)       
        return s
    
    """ [Backward] Recursively build upon subsets of smaller size: O(2^n) """
    def subsetsWithDupRecursiveSuffix(self, nums): 
        nums.sort() # sort!
        return self.subsetsWithDupRecursiveSuffixHelper(nums, 0)[0]
    
    def subsetsWithDupRecursiveSuffixHelper(self, nums, p):
        if p == len(nums): return [[]], 0 # !
        
        subres, latest = self.subsetsWithDupRecursiveSuffixHelper(nums, p+1)
        res = deepcopy(subres)
        
        if p+1 < len(nums) and nums[p+1] != nums[p]:
            latest = 0 # non-dup
   
        for s in subres[latest:]:
            s.append(nums[p])          
            res.append(s)
            
        return res, len(subres)


    """ [Forward] Recursively build upon subsets of smaller size: O(2^n + n^2) = O(2^n) """
    def subsetsWithDupRecursivePrefix(self, nums):
        nums.sort() # sort!
        result, results = [], [[]] # !
        self.subsetsWithDupRecursivePrefixHelper(nums, result, results, 0)     
        return results

    def subsetsWithDupRecursivePrefixHelper(self, nums, result, results, p):       
        for i in range(p, len(nums)): # decide what to put at pth position
            if i != p and nums[i] == nums[i-1]: continue
            result.append(nums[i])
            results.append(deepcopy(result))
            self.subsetsWithDupRecursivePrefixHelper(nums, result, results, i+1)
            result.pop()


