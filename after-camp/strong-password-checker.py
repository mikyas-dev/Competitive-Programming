MAGIC = "abAB01"


def new_mask(mask: int, c: str) -> int:
    if c in string.ascii_lowercase:
        return mask | 1
    if c in string.ascii_uppercase:
        return mask | 2
    return mask | 4


def new_repeat(repeat: str, c: str) -> str:
    if not repeat or repeat[-1] != c:
        return c
    return repeat + c


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        mx = 70

        @functools.cache
        def dp(position: int, length: int, mask: int, repeat: str) -> int:
            if length > 20 or len(repeat) >= 3:
                return mx

            if position == len(password):
                if 6 <= length and mask == 0b111:
                    return 0
                return mx

            # no change
            ans = dp(position + 1, length + 1, new_mask(mask, password[position]), new_repeat(repeat, password[position]))

            # insert
            for c in MAGIC:
                ans = min(ans, 1 + dp(position, length + 1, new_mask(mask, c), new_repeat(repeat, c)))

            # delete
            ans = min(ans, 1 + dp(position + 1, length, mask, repeat))

            # replace
            for c in MAGIC:
                ans = min(ans, 1 + dp(position + 1, length + 1, new_mask(mask, c), new_repeat(repeat, c)))

            return ans

        return dp(0, 0, 0, '')