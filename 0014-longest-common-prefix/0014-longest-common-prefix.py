class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        strs = sorted(strs)
        word = strs[0]  # The smallest string

        for i in range(len(word)):
            if strs[0][i] == strs[-1][i]:
                answer += strs[0][i]
            else:
                break
        return answer