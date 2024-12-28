from collections import Counter

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(Counter(citations).items() , key = lambda pair : pair[0], reverse = True)
        
        ci_sum = 0
        for (cc, ci) in citations :
            if ci_sum >= cc:
                return ci_sum
            ci_sum += ci
            if ci_sum >= cc:
                return cc
        
        return ci_sum if ci_sum > 1 else 1