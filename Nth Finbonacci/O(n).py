class Solution:
    def tribonacci(self, n: int) -> int:
        F = []
        F.append(0)
        F.append(1)
        F.append(1)
        if n == 0:
            return F[0]
        while len(F) <= n:
            F.append(F[len(F) - 3] + F[len(F) - 2] + F[len(F) - 1])
        return F[len(F) - 1]