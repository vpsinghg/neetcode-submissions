class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=(str(len(s))+"#"+s)
        return res

    def decode(self, s: str) -> List[str]:
        i=0;
        total=len(s)
        res= []

        while(i<total):
            j=i
            while(j<total and s[j]!="#"):
                j+=1
            str_size=int(s[i:j])
            if(str_size>0):
                till = j+1+str_size
                res.append(s[j+1:j+1+str_size])
                i= till
            else:
                res.append("")
                i = j+1
        return res

