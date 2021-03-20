class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs={}
        #mapping
        for str in strs:
            if tuple(sorted(str)) in dict_strs.keys():
                dict_strs[tuple(sorted(str))].append(str)
            else: dict_strs[tuple(sorted(str))]=[str]
        print(dict_strs)
        
        return list(dict_strs.values())
