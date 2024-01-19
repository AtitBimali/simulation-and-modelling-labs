import random

def f(x):
    return x**2

n = int(input("Enter the number of random samples: "))
integral = 0.0

for i in range(n):
    x = random.uniform(0, 1)  # Random x between 0 and 1
    y = random.uniform(0, 1)  # Random y between 0 and 1

    if y <= f(x):
        integral += 1.0

estimated_integral = integral / n
print(f"Estimated value of the integral: {estimated_integral}\n")
