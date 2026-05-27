class Solution:
    def reverseWords(self, s: str) -> str:
        d=s.split()
        n=len(d)
        r=[]
        print(n)
        for i in range(n-1,-1,-1):
            r.append(d[i])
        return " ".join(r)
        
