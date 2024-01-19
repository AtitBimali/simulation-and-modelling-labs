import random

n = int(input("\nEnter the number of random samples: "))
C_point = 0
S_point = 0

for i in range(n):
    x = random.uniform(0, 1)  # Random x between 0 and 1
    y = random.uniform(0, 1)  # Random y between 0 and 1
    distance = x * x + y * y

    if distance <= 1:
        C_point += 1

    S_point += 1

estimated_pi = 4 * (C_point / S_point)
print(f"\nEstimated value of pi: {estimated_pi}\n")
