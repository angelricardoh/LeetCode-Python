import math

class Solution:    
    def countPrimes(self, n: int) -> int:
        primes = []
        
        if n == 0 or n == 1:
            return 0
        
        for i in range(2, n):
            primes.append(i)
            for j in range(2, i):
                if i % j == 0:
                    primes.remove(i)
                    break

        return len(primes)

    def countPrimesSqrtTime(self, n: int) -> int:
        # primes = {}
        not_primes = {0, 1}
        
        if n < 2:
            return 0
        
        for i in range(2, int(math.sqrt(n) + 1)):
            if i not in not_primes:
                for j in range(i + i, n + 1, i):
                    not_primes.add(j)
                
        return n - len(not_primes)

solution = Solution()
print(solution.countPrimesSqrt(-1))
print(solution.countPrimesSqrt(0))
print(solution.countPrimesSqrt(1))
print(solution.countPrimesSqrt(2))
print(solution.countPrimesSqrt(7))
print(solution.countPrimesSqrt(1000))