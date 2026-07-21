class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n+1)]
    
        for i in range(1,n+1):
            power_2 = int(math.log(i,2))
            if((i&(i-1)) == 0):
                res[i]=1
            else:
                res[i]=1+res[i-2**power_2]        
        return res
        