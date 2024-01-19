a = 27
m = 100 

def multiplicative_linear_congruential(seed):
    return (a * seed) % m

if __name__ == "__main__":
    seed = int(input("Enter a seed value: "))
    num_random_numbers = int(input("Enter the number to be generate: "))

    print("Generated Random Numbers:")
    for i in range(num_random_numbers):
        seed = multiplicative_linear_congruential(seed)
        print(f"Random Number {i + 1}: {seed}")
