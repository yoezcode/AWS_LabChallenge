## Display all the prime numbers between 1 to 250. Store results in a results.txt file

print("Running script to calculate all prime numbers between 1 - 250...")
def primes_in_range(start, end):
    primes = []
    #  +1 to include 250 in the range
    for n in range(start, end +1):
        if n > 1:
            is_prime = True
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(n)
    return primes

def write_to_file(primes):
    with open("results.txt", "w") as file:
        file.write(f"{primes}")
  
  
result_of_primes = primes_in_range(1, 150)

print("Finished. Writing result to file...")
to_file = write_to_file(result_of_primes)

print("Finished.")

