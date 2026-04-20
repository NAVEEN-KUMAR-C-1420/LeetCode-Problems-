class Solution:
    def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
        res=[]
        for i in candies:
            if i+extra>=max(candies):
                res.append(True)
            else:
                res.append(False)
        return res