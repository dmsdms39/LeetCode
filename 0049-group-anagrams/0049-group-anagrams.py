class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        anagram_dict = defaultdict(list)
        
        for letter in strs:
            anagram_dict[''.join(sorted(letter))].append(letter)

        return list(anagram_dict.values())

        