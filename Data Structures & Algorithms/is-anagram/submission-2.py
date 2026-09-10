class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        cs = sorted(s)
        ct = sorted(t)
        if cs == ct:
            return True 
        else:
            return False
    
            
               
