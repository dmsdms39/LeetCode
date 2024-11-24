class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        minval = 1e9
        minpos = -1
        ptrol = 0
        for i in range(len(gas)):
            ptrol += gas[i]-cost[i]
            if ptrol < minval:
                minval = ptrol
                minpos = i
        if ptrol >= 0:
            return (minpos+1) % len(gas)
        return -1       