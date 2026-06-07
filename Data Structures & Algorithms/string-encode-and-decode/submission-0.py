class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ''
        for s in strs:
            encode_str += (str(len(s)) + '#' + s )
        
        return encode_str

    def decode(self, s: str) -> List[str]:
        result = []
        temp_num = int()
        i = 0

        while i < len(s) - 1:
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            result.append(s[i:i+length])

            i += length

        return result


