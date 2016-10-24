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
            for elem in deepcopy(s):
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


    """ [Forward/Prefix] Recursively build upon subsets of smaller size: O(2^n) """
    def subsetsRecursivePrefix(self, nums):       
        s = [[]]
        self.subsetsRecursivePrefixHelper(nums, 0, s)     
        return results

    def subsetsRecursivePrefixHelper(self, nums, p, s):       
        if p == len(nums): return
        for sub in deepcopy(s):
            sub.append(nums[p])
            s.append(sub)
        self.subsetsRecursivePrefixHelper(nums, p+1, s)


    """ [Backward/Suffix] Recursively build upon subsets of smaller size: O(2^n) """
    def subsetsRecursiveSuffix(self, nums):       
        return self.subsetsRecursiveSuffixHelper(nums, 0)
    
    def subsetsRecursiveSuffixHelper(self, nums, p):
        if p == len(nums): return [[]] # !     
        subs = self.subsetsRecursiveSuffixHelper(nums, p+1)
        s = deepcopy(subres)
        for sub in subs:
            sub.append(nums[p])          
            s.append(sub)      
        return s


    """ [Backtracking] Recursively decide what to put next: O(2^n + n^2) = O(2^n) """
    def subsetsRecursiveBacktracking(self, nums):       
        sub, subs = [], [[]] # !
        self.subsetsRecursiveBacktrackingHelper(nums, sub, subs, 0)     
        return results

    def subsetsRecursiveBacktrackingHelper(self, nums, sub, subs, p):       
        for i in range(p, len(nums)): # explore all options        
            sub.append(nums[i])
            subs.append(deepcopy(sub))
            self.subsetsRecursiveBacktrackingHelper(nums, sub, subs, i+1) # i+1, larger index only
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
    

    """ [Forward/Prefix] Recursively build upon subsets of smaller size: O(2^n) """
    def subsetsWithDupRecursivePrefix(self, nums):
        nums.sort() # sort!
        s = [[]]
        self.subsetsWithDupRecursivePrefixHelper(nums, 0, s, 0)     
        return s

    def subsetsWithDupRecursivePrefixHelper(self, nums, p, s, latest):       
        if p == len(nums): return
        subs = deepcopy(s)
        if p > 0 and nums[p] != nums[p-1]: latest = 0
        for sub in subs[latest:]:
            sub.append(nums[p])
            s.append(sub)
        self.subsetsWithDupRecursivePrefixHelper(nums, p+1, s, len(subs))
        
    
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


    """ [Backtracking] Recursively decide what to put next: O(2^n + n^2) = O(2^n) """
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


    #46. Permutations
    """ Swapping method. But essentially, it is building upon solutions to same problem of
        smaller sizes in a recursive way (which can be proved by induction)
    """
    def permute(self, nums):
        rs = []
        self.permuteHelper(0, nums, rs)        
        return rs

    def permuteHelper(self, p, nums, rs):
        if p == len(nums) - 1:
            rs.append(nums[:])

        for i in range(p, len(nums)):
            nums[i], nums[p] = nums[p], nums[i]
            self.permuteHelper(p+1, nums, rs)
            nums[i], nums[p] = nums[p], nums[i]

    """ Figure out the difference in examples where there is dups.
        Need to avoid swapping with identicals to create same braching nodes. (not sufficient)
        Actually need to avoid placing the same number to a particular position. """
    def permuteUnique(self, nums):
        rs = []
        self.permuteUniqueHelper(0, nums, rs)        
        return rs
    
    def permuteUniqueHelper(self, p, nums, rs):
    def permuteUnique(self, nums):
        rs = []
        self.permuteUniqueHelper(0, nums, rs)        
        return rs
    
    def permuteUniqueHelper(self, p, nums, rs):
        if p == len(nums) - 1:
            rs.append(nums[:])
            return # don't forget
        
        visited = set()
        for i in range(p, len(nums)):
            #if i > p and nums[i] == nums[p]: continue (problematic)
            if i > p and nums[i] in visited: continue
            visited.add(nums[i])
            nums[i], nums[p] = nums[p], nums[i]
            self.permuteUniqueHelper(p+1, nums, rs)
            nums[i], nums[p] = nums[p], nums[i]        
