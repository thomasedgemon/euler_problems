#find sum of even-valued fibonacci terms less than or equal to four million. 
fibonacci = [1,2,3,5]
fibonacci_even = []
  
while fibonacci[-1] <= 4000000:
  fibonacci.append(fibonacci[-1] + fibonacci[-2])
  
for n in fibonacci:
  if n % 2 == 0:
    fibonacci_even.append(n)

print(sum(fibonacci_even))
_________________________________________________________________________
#what is the largest prime factor of 600851475143?

from math import isqrt
factors_of_n = []
prime_factors = []
composite_factors = []
bignum = 600851475143
bignum_root = isqrt(bignum)
#find factors and reverse sort
for x in range(1, bignum_root - 1):
      if bignum % x == 0:
        factors_of_n.append(x)
        factors_of_n.sort(reverse=True) #reverse-sorted list of bignum factors
 
def is_prime():
  for n in factors_of_n:
    prime = True
    for i in range(2, isqrt(n)+1):
      if n % i == 0:
        prime = False
        break
    if prime:
      if n not in prime_factors:
        prime_factors.append(n)

          
is_prime()

print("factors are")
print(factors_of_n)    
print("prime factors are")
print(prime_factors)
_________________________________________________
#find the largest palindrome number made from the product of two 3 digit numbers.

products = []
palindromes = []
#find all products. no need to store its divisors.
for i in range(900, 999):
  for j in range(900, 999):
    if i * j in products:
      pass
    else:
      products.append(i * j )
#test for palindromicitiy
def palindromicity():
  for x in products:
    x = str(x)
    if x[0] == x[-1]:
      if x[1] == x[-2]:
        if x[2] == x[-3]:
          palindromes.append(x)
  
palindromicity()
palindromes.sort(reverse=True)
print(palindromes[0])








