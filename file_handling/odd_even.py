import math
def is_prime(N):
    n = math.floor(math.sqrt(N))
    for val in range(2,n+1):
        if N%val==0:
            return 0
    return 1

input_file = 'file_handling\\random_numbers.txt'
even_file = 'even_numbers.txt'
odd_file = 'odd_numbers.txt'
prime_file = 'prime_numbers.txt'

with open(input_file, "rt") as file:
    numbers = list(map(int, file.read().split()))

even_numbers = []
odd_numbers = []
prime_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
    if is_prime(number):
        prime_numbers.append(number)

with open(even_file, "w") as file:
    file.write("\n".join(map(str, even_numbers)))
    
    
with open(odd_file, "w") as file:
    file.write("\n".join(map(str, odd_numbers)))
    

with open(prime_file, "w") as file:
    file.write("\n".join(map(str, prime_numbers)))
    
print("Numbers have been categorized and written to respective files.")