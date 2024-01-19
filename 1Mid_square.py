def mid_square(seed, n):
    random_numbers = []
    for _ in range(n):
        seed = int(str(seed**2).zfill(8)[2:6])  # Square, pad with zeros, and take middle 4 digits
        random_numbers.append(seed)
    return random_numbers

# Usage
seed_value = int(input("Enter a seed value: "))  # Use a larger seed value
num_random_numbers = int(input("Enter the number to generate: "))

random_numbers = mid_square(seed_value, num_random_numbers)
for i, num in enumerate(random_numbers, start=1):
    print(f"Random Number {i}: {num}")
