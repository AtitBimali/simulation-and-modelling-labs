import numpy as np
from scipy.stats import chi2

def poker_test(random_numbers):
    # Convert random numbers to integers for simplicity
    integer_numbers = (random_numbers * 10000).astype(int)

    # Set parameters for the Poker Test
    group_size = 9
    num_groups = len(integer_numbers) // group_size

    # Initialize a dictionary to count occurrences of each pattern
    pattern_counts = {}

    # Perform Poker Test
    for i in range(num_groups):
        group = tuple(integer_numbers[i * group_size : (i + 1) * group_size])
        pattern_counts[group] = pattern_counts.get(group, 0) + 1

    # Calculate chi-square statistic
    observed_frequencies = np.array(list(pattern_counts.values()))
    
    # Set different expected frequencies (for illustration purposes)
    expected_frequencies = np.ones_like(observed_frequencies) * (num_groups / len(pattern_counts) + 1)

    chi2_statistic = np.sum((observed_frequencies - expected_frequencies) ** 2 / expected_frequencies)

    # Calculate degrees of freedom
    degrees_of_freedom = len(pattern_counts) - 1

    # Perform chi-square test
    significance_level = 0.05
    critical_value = chi2.ppf(1 - significance_level, degrees_of_freedom)

    # Print results
    print("\nHypothesis:")
    print(f"H0 : The sequence of numbers is independent.")
    print(f"H1 : The sequence of numbers is not independent.")
    print("\nChi-Square Statistic:", round(chi2_statistic, 3))
    print("Degrees of Freedom:", degrees_of_freedom)
    print("Critical Value:", round(critical_value, 3))

    # Hypothesis testing
    if chi2_statistic > critical_value:
        print(f"\nResult: Reject H0 at {significance_level} significance level.")
        print("Conclusion: The sequence of numbers is not independent.")
    else:
        print(f"\nResult: Fail to reject H0 at {significance_level} significance level.")
        print("Conclusion: The sequence of numbers is independent.")

if __name__ == "__main__":
    # Generate random numbers (replace this with your own random numbers)
    np.random.seed(42)
    random_numbers = np.random.rand(1000)

    # Perform Poker Test
    poker_test(random_numbers)
