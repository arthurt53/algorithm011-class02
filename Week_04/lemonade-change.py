class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i=j=0
        for k in bills:
            if k==5:i+=1
            elif k==10:j+=1;i-=1
            else:
                if j==0:i-=3
                else:i-=1;j-=1
            if i<0 or j<0:return False
        return True
