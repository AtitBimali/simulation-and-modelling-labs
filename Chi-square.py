import numpy as np
from scipy.stats import chi2_contingency

# Generate random numbers (uniform distribution)
np.random.seed(50)  # Set seed for reproducibility
random_numbers = np.random.uniform(0, 1, 1000)

def chi_square_test_uniformity(data):
    # Define the number of bins for the chi-square test
    num_bins = 10

    # Perform chi-square test for uniformity
    observed, bin_edges = np.histogram(data, bins=num_bins)
    expected = np.full_like(observed, fill_value=len(data) / num_bins)
    
    chi2_statistic, chi2_p_value, _, _ = chi2_contingency([observed, expected])

    # Round Chi-Square statistic and p-value to 5 decimal places
    chi2_statistic = round(chi2_statistic, 5)
    chi2_p_value = round(chi2_p_value, 5)

    print("\nHypothes is:")
    print(f"H0 : The distribution is uniform.")
    print(f"H1 : The distribution is not uniform.")
    print("\nChi-Square Statistic:", chi2_statistic)
    print("P-value:", chi2_p_value)

    # Hypothesis testing
    significance_level = 0.05

    if chi2_p_value < significance_level:
        print(f"\nResult: Reject H0 at {significance_level} significance level.")
        print("Conclusion: The distribution is likely not uniform.")
    else:
        print(f"\nResult: Reject H1 at {significance_level} significance level.")
        print("Conclusion: The distribution is likely uniform.")

if __name__ == "__main__":
    chi_square_test_uniformity(random_numbers)
