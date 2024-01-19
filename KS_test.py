import numpy as np
from scipy.stats import kstest

# Generate random numbers (uniform distribution)
np.random.seed(42)  # Set seed for reproducibility
random_numbers = np.random.uniform(0, 1, 1000)


def ks_test_uniformity(data):
    # K-S test for uniformity
    ks_statistic, ks_p_value = kstest(data, 'uniform')

    # Round K-S statistic and p-value to 5 decimal places
    ks_statistic = round(ks_statistic, 5)
    ks_p_value = round(ks_p_value, 5)

    print("\nHypothesis:")
    print(f"H0 : The distribution is uniform.")
    print(f"H1 : The distribution is not uniform.")
    print("\nK-S Statistic:", ks_statistic)
    print("P-value:", ks_p_value)

    # Hypothesis testing
    significance_level = 0.05

    if ks_p_value < significance_level:
        print(
            f"\nResult: Reject H0 at {significance_level} significance level.")
        print("Conclusion: The distribution is likely not uniform.")
    else:
        print(f"\nResult: Reject H1 at {significance_level} significance level.")
        print("Conclusion: The distribution is likely uniform.")


if __name__ == "__main__":
    ks_test_uniformity(random_numbers)
