class Solution:
    def getHashKey(self, s):
        frequency = [0] * 26

        for ch in s:
            frequency[ord(ch) - ord('a')] += 1

        res = ""
        for i in range(26):
            if frequency[i] != 0:
                res += chr(ord('a') + i) + str(frequency[i])

        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        for s in strs:
            hash_key = self.getHashKey(s)
            if(hash_key in hash_map.keys()):
                hash_map[hash_key].append(s)
            else:
                hash_map[hash_key]=[s]
        res =[]
        for _, group in hash_map.items():
            res.append(group)
        return res



        