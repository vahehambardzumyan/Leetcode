class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        a, b  = a[::-1],b[::-1]
        res=[]
        i = 0
        carry = 0
        while i < len_b or i< len_a or carry:

            x =  int(a[i]) if  len_a >i else 0 
            y =  int(b[i]) if  len_b >i else 0 

            total = x + y + carry

            res.append(str(total%2))
            carry= total//2
            i+=1
                 
        return  ''.join(res[::-1])
        