"""
Project Euler Problem 3
The prime factors of 13195
are 5, 7, 13 and 29. What is the largest prime factor of the number 600 851 475 143 ?
"""
import math
class Solution:

    def __init__(self):
        self.factors = []
        self.prime_factors = []

    def get_factors(self, target_no):
        for factor in range(1, int(math.sqrt(target_no))+1):
            if target_no % factor == 0:
                self.add_factor(factor)
                if self.check_prime(factor):
                    self.add_prime_factor(factor)

    def add_factor(self, factor):
        self.factors.append(factor)

    def check_prime(self, number):
        prime = True
        for x in range(1, int(math.sqrt(number))+1):
            if (x != 1) and (number % x == 0):
                prime = False
                print(f"{number} is not prime")
                break

        if prime == True:
            print(f"{number} is prime")

            return True
        else:
            return False

    def print_factors(self):
        print(self.factors)

    def print_prime_factors(self):
        print(self.prime_factors)

    def add_prime_factor(self, number):
        self.prime_factors.append(number)

attempt = Solution()
attempt.get_factors(600851475143)
attempt.print_factors()
attempt.print_prime_factors()






