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
//golang
//find first ten digits of the sum of 100 50-digit numbers
package main

import (
	"fmt"
	"math/big"
)

// work out the first ten digits of the sumof the sum of the following
// one hundred 50 digit numbers
var numStrings = []string{
	"37107287533902102798797998220837590246510135740250",
	"46376937677490009712648124896970078050417018260538",
	"74324986199524741059474233309513058123726617309629",
	"91942213363574161572522430563301811072406154908250",
	"23067588207539346171171980310421047513778063246676",
	"89261670696623633820136378418383684178734361726757",
	"28112879812849979408065481931592621691275889832738",
	"44274228917432520321923589422876796487670272189318",
	"47451445736001306439091167216856844588711603153276",
	"70386486105843025439939619828917593665686757934951",
	"62176457141856560629502157223196586755079324193331",
	"64906352462741904929101432445813822663347944758178",
	"92575867718337217661963751590579239728245598838407",
	"58203565325359399008402633568948830189458628227828",
	"80181199384826282014278194139940567587151170094390",
	"35398664372827112653829987240784473053190104293586",
	"86515506006295864861532075273371959191420517255829",
	"71693888707715466499115593487603532921714970056938",
	"54370070576826684624621495650076471787294438377604",
	"53282654108756828443191190634694037855217779295145",
	"36123272525000296071075082563815656710885258350721",
	"45876576172410976447339110607218265236877223636045",
	"17423706905851860660448207621209813287860733969412",
	"81142660418086830619328460811191061556940512689692",
	"51934325451728388641918047049293215058642563049483",
	"62467221648435076201727918039944693004732956340691",
	"15732444386908125794514089057706229429197107928209",
	"55037687525678773091862540744969844508330393682126",
	"18336384825330154686196124348767681297534375946515",
	"80386287592878490201521685554828717201219257766954",
	"78182833757993103614740356856449095527097864797581",
	"16726320100436897842553539920931837441497806860984",
	"48403098129077791799088218795327364475675590848030",
	"87086987551392711854517078544161852424320693150332",
	"59959406895756536782107074926966537676326235447210",
	"69793950679652694742597709739166693763042633987085",
	"41052684708299085211399427365734116182760315001271",
	"65378607361501080857009149939512557028198746004375",
	"35829035317434717326932123578154982629742552737307",
	"94953759765105305946966067683156574377167401875275",
	"88902802571733229619176668713819931811048770190271",
	"25267680276078003013678680992525463401061632866526",
	"36270218540497705585629946580636237993140746255962",
	"24074486908231174977792365466257246923322810917141",
	"91430288197103288597806669760892938638285025333403",
	"34413065578016127815921815005561868836468420090470",
	"23053081172816430487623791969842487255036638784583",
	"11487696932154902810424020138335124462181441773470",
	"63783299490636259666498587618221225225512486764533",
	"67720186971698544312419572409913959008952310058822",
	"95548255300263520781532296796249481641953868218774",
	"76085327132285723110424803456124867697064507995236",
	"37774242535411291684276865538926205024910326572967",
	"23701913275725675285653248258265463092207058596522",
	"29798860272258331913126375147341994889534765745501",
	"18495701454879288984856827726077713721403798879715",
	"38298203783031473527721580348144513491373226651381",
	"34829543829199918180278916522431027392251122869539",
	"40957953066405232632538044100059654939159879593635",
	"29746152185502371307642255121183693803580388584903",
	"41698116222072977186158236678424689157993532961922",
	"62467957194401269043877107275048102390895523597457",
	"23189706772547915061505504953922979530901129967519",
	"86188088225875314529584099251203829009407770775672",
	"11306739708304724483816533873502340845647058077308",
	"82959174767140363198008187129011875491310547126581",
	"97623331044818386269515456334926366572897563400500",
	"42846280183517070527831839425882145521227251250327",
	"55121603546981200581762165212827652751691296897789",
	"32238195734329339946437501907836945765883352399886",
	"75506164965184775180738168837861091527357929701337",
	"62177842752192623401942399639168044983993173312731",
	"32924185707147349566916674687634660915035914677504",
	"99518671430235219628894890102423325116913619626622",
	"73267460800591547471830798392868535206946944540724",
	"76841822524674417161514036427982273348055556214818",
	"97142617910342598647204516893989422179826088076852",
	"87783646182799346313767754307809363333018982642090",
	"10848802521674670883215120185883543223812876952786",
	"71329612474782464538636993009049310363619763878039",
	"62184073572399794223406235393808339651327408011116",
	"66627891981488087797941876876144230030984490851411",
	"60661826293682836764744779239180335110989069790714",
	"85786944089552990653640447425576083659976645795096",
	"66024396409905389607120198219976047599490197230297",
	"64913982680032973156037120041377903785566085089252",
	"16730939319872750275468906903707539413042652315011",
	"94809377245048795150954100921645863754710598436791",
	"78639167021187492431995700641917969777599028300699",
	"15368713711936614952811305876380278410754449733078",
	"40789923115535562561142322423255033685442488917353",
	"44889911501440648020369068063960672322193204149535",
	"41503128880339536053299340368006977710650566631954",
	"81234880673210146739058568557934581403627822703280",
	"82616570773948327592232845941706525094512325230608",
	"22918802058777319719839450180888072429661980811197",
	"77158542502016545090413245809786882778948721859617",
	"72107838435069186155435662884062257473692284509516",
	"20849603980134001723930671666823555245252804609722",
	"53503534226472524250874054075591789781264330331690",
}

func main() {
	summation := big.NewInt(0)
	//init empty slice to store first ten digits of final sum
	for _, str := range numStrings {
		n := new(big.Int)
		n, ok := n.SetString(str, 10)
		if !ok {
			fmt.Println("invalid number", str)
			return
		}

		summation.Add(summation, n)
	}
	sumStr := summation.String()
	fmt.Println("first ten digits", sumStr[:10])
}
____________________________________________

//golang
//find the number less than one million wich has the longest collatz sequence
package main

import (
	"fmt"
)

func isEven(n int) bool {
	return n%2 == 0
}

// recursive function that returns the length of the sequence
func collatzLength(n int) int {
	if n == 1 {
		return 1
	}
	if isEven(n) {
		return 1 + collatzLength(n/2)
	}
	return 1 + collatzLength(3*n+1)
}

// define a struct to hold the start number and its sequence length
type CollatzInfo struct {
	start  int
	length int
}

func main() {
	var maxInfo CollatzInfo // zero value will be (0, 0)

	for i := 1; i < 1000000; i++ {
		length := collatzLength(i)
		if length > maxInfo.length {
			maxInfo = CollatzInfo{start: i, length: length}
		}
	}

	fmt.Println("Starting number with the longest Collatz sequence:", maxInfo.start)
	fmt.Println("Length of sequence:", maxInfo.length)
}
____________________________
//golang












