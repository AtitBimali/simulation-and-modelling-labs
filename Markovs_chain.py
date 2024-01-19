import numpy as np

def markov_chain_probability(initial_state_prob, transition_matrix, num_steps):
    current_prob = initial_state_prob
    for _ in range(num_steps):
        current_prob = np.dot(current_prob, transition_matrix)
    return current_prob

# Define the transition matrix
transition_matrix = np.array([[0.4, 0.6], [0.8, 0.2]])

# Define the initial state probability vector
initial_state_prob = np.array([0, 1])  # Starting with Fanta

# Number of steps (purchases)
num_steps = 2

# Calculate the probability vector after 2 purchases
result_prob = markov_chain_probability(initial_state_prob, transition_matrix, num_steps)

# The probability of drinking Coke after 2 purchases if the person has drunk Fanta again
probability_of_coke_after_2_purchases = result_prob[0]

print(f"Probability of drinking Coke after 2 purchases if the person has drunk Fanta again is {probability_of_coke_after_2_purchases:.4f}")
