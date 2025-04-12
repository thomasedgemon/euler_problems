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
__________________________
#NOT COMPUTATIONALLY FEASIBLE, BUT WORKS
#what is smallest number that is divisible by all numbers one through twenty?

possibles = []
divisors = [4,11,12,13,14,15,16,17,18,19,20,21]

for x in range(1, 300000000):
  potential = True
  for i in divisors:
    if x % i == 0:
      potential &= True
    else:
      potential &= False
  if potential and x not in possibles:
      possibles.append(x)

    

      
possibles.sort
print(possibles)
________________________________________________________
#find the difference between the sum of the squares and the square of the sums of the first 100 natural numbers

import math

def sum_of_squares(n):
    return (((n**2)+n)*((2*n)+1)) / 6
    
def square_of_sums(n):
    sums_squared = 0
    sum = 0
    for i in range(1, n+1):   
        sum = sum + i
    
    sums_squared = sum ** 2
    return sums_squared

a = square_of_sums(100)
b = sum_of_squares(100)

print(a-b)
_____________________________________________________________
#what is smallest number evenly divisible by all number from one to twenty?
num = 20
smallest = []
found = False
def test():
    global num
    for i in range(2, 21):
        if num % i == 0:
            good = True
        else:
            good = False
            num += 20
            break
    
    if good == True:
        found = True
        print(num)

while found == False:
    test()

#what is the 10001st prime number


primes = [1,3,5,7,11]
number = 12

while len(primes) < 10001: 
    if all(number % i != 0 for i in range(2, number)):
        #print(f"{number} is prime")
        primes.append(number)
        #print(f"appended {number} to primes list")
        number += 1
    else:
        #print(f"{number} is not prime")
        number += 1


print(primes[-1])

____________________________________________________________________________
#which 13 adjacent digits in a large number have the highest product?
import math
#if there is a zero, skip that product
largest_product = 0
position = 0
temp = []

while position < 987:
    for i in range(position, position + 13):
        converted = int(number[i])
        temp.append(converted)
    
    print(temp)
    product = math.prod(temp)
    print(f"product:, {product}")
    if product > largest_product:
        largest_product = product
        print(largest_product)

    position += 1
    temp = []

print(f"largest product: {largest_product}")
__________________________________________________________________
# pythagorean triplet: a < b < c, and a^2 + b^2 = c^2
#there is only one set of a, b, and c triplet such that a + b + c = 1000. what is the product of a, b, and c?
import math
import time

for a in range(1,999):
    for b in range(1,999):
        c_squared = (a**2) + (b**2)
        c = math.sqrt(c_squared)
        if a + b + c == 1000:
            product = a * b * c
            print(product)
________________________________________________
//this is written in golang
//find the first triangular number with at least 500 divisors
import "fmt"

func triangle_number(n int) int {
	sum := 0
	for i := 1; i <= n; i++ {
		sum += i
	}
	return sum
}
func main() {
	var n int = 1

	for {
		answer := triangle_number(n)
		num_divisors := 0

		for i := 1; i <= answer; i++ {
			if answer%i == 0 {
				num_divisors += 1
			}
		}

		if num_divisors >= 500 {
			fmt.Printf("The first triangle number that has at least 500 divisors is %d\n", answer)
			break
		}

		n += 1
	}
}
___________________________________












