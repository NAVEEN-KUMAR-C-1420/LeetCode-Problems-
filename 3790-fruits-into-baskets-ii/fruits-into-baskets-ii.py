class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for i in fruits:
            for j in range(len(baskets)):
                if baskets[j]>=i:
                    baskets[j]=0
                    break
        print(baskets)
        return len(baskets)-baskets.count(0)