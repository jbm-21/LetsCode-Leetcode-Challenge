class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
      
     a=0 #position
     b=0 #count
     for i in nums:
         a+=i
         if a==0:
             b+=1
     return b        
