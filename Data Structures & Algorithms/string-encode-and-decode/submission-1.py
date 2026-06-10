class Solution:

    def encode(self, strs: List[str]) -> str:
        encrypt_strs = str()
        for i in strs:
            encrypt_strs = encrypt_strs + str(len(i)) + '#' + i 
        
        return encrypt_strs

    def decode(self, s: str) -> List[str]:
        i = 0
        result = list()

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            
            i = j + length + 1
        
        return result
            







