class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        a = e = i = o = u = 1
         
        for _ in range(n-1):
            new_a = e + i + u
            new_e = a + i
            new_i = e + o
            new_o = i
            new_u = i + o

            a, e, i, o, u = (
                new_a % MOD,
                new_e % MOD,
                new_i % MOD,
                new_o % MOD,
                new_u % MOD
            )
        return (a + e + i + o + u) % MOD

        