# Define constants (change these for different sequences)
a = 27
c = 4
m = 100

def linear_congruential(seed):
    current = seed
    while True:
        current = (a * current + c) % m
        yield current

if __name__ == "__main__":
    seed = int(input("Enter a seed value : "))
    num_random_numbers = int(input("Enter the number to be generate: "))

    if seed == 0:
        import time
        seed = int(time.time())

    generator = linear_congruential(seed)

    print("Generated Random Numbers:")
    for i in range(num_random_numbers):
        random_number = next(generator)
        print(f"Random Number {i + 1}: {random_number}")
