class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=0
        count=0
        for x in nums:
            if x%3==0 and x%2==0:
                s+=x
                count+=1
        if count==0:
            return 0         
        return s//count 
