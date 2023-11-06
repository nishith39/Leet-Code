class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            next_num = 0
            while n > 0:
                digit = n % 10
                next_num += digit ** 2
                n //= 10
            return next_num

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
