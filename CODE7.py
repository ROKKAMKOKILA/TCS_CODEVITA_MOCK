# 13) Consecutive Prime Sum
# Some prime numbers can be expressed as the sum of other consecutive prime numbers.
# For example
# 5 = 2 + 3
# 17 = 2 + 3 + 5 + 7
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
# Write the code to find out the number of prime numbers that satisfy the above mentioned property in a given range.
 
# Input Format:
# First line contains a number N
# Output Format:
# Print the total number of all such prime numbers which are less than or equal to N.
# Constraints: 2<N<=1,200,000,000
# Sample Test Case 1:
# Input:
# 20
# Output:
# 2
# Explanation: Below 20 we have 2 such numbers 5 and 17
import math
def is_prime(b):
    for i in range(2, int(math.sqrt(b)) + 1):
        if b % i == 0:
            return False
    return True

def main():
    n = int(input())
    count = 0
    sum_primes = 2 

    for i in range(3, n + 1):
        if is_prime(i):
            sum_primes += i
            if is_prime(sum_primes) and sum_primes <= n:
                count += 1
                
    print(count)

if __name__ == "_main_":
    main()
