class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            if direction == 1:
                prefix[start] += 1
                prefix[end + 1] -= 1
            else:
                prefix[start] -= 1
                prefix[end + 1] += 1
        
        res = []
        for i, c in enumerate(s):
            shift = prefix[i]
            res.append(chr(((ord(c) - 97 + shift) % 26) + 97))
            prefix[i + 1] += prefix[i]
        return "".join(res)