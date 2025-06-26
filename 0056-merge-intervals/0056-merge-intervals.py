class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])

        result = [intervals[0]]

        for s, e in intervals:
            lastE = result[-1][1] 
            if lastE >= s :
                if lastE < e :
                    result[-1][1] = e
            else :
                result.append([s, e])

        return result