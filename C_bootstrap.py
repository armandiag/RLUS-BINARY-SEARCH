import numpy as np


def bootstrap(theta, n, delta_target, q, b):
    theta = np.asarray(theta).flatten()
    n = min(n, len(theta))
    n = int(n) 
    print(f"n: {n}")

    # if len(theta) == 0:
    #     raise ValueError("Input data (theta) is empty.")

    # if n <= 0 or not isinstance(n, int):
    #     raise ValueError("Sample size (n) must be a positive integer.")

    # if n > len(theta):
    #     n = len(theta)  # Adjust n to the maximum allowable size

    epsilons = []

    S_0 = np.random.choice(theta, size=n, replace=True)
    # median_S_0 = np.median(S_0)  # Calculate the median of the sample
    # difference_median = median_theta - median_S_0  # Calculate the difference
    # median_differences.append(difference_median)  # Optionally store difference_median if needed

    x_0 = np.quantile(S_0, q)
    # print(f"x_0: {x_0}")

    for _ in range(b):
        S_i = np.random.choice(theta, size=n, replace=True)
        # median_S_i = np.median(S_i)  # Calculate the median of the sample
        # difference_median = median_theta - median_S_i  # Calculate the difference
        # median_differences.append(difference_median)  # Optionally store difference_median if needed
        x_i = np.quantile(S_i, q)
        # print(f"abs(x_i - x_0)): {abs(x_i - x_0)}")
        epsilons.append(abs(x_i - x_0))

    # Diagnostic print to inspect the first few epsilon values
    # print("First few epsilon values:", epsilons[:100])
    epsilons.sort()

    # Calculate the index to select epsilon
    s_index = int(1 + b * (delta_target / 2)) - 1
    # difference_median_epsilon=difference_median-epsilons[s_index]
    print(f"s_index: {s_index}")
    print(f"epsilons[s_index]: {epsilons[s_index]}")

    return epsilons[s_index]

    # return {
    #     "difference_median": difference_median,
    #     "current_epsilon": epsilons[s_index],
    #     "difference_median_epsilon": difference_median_epsilon,
    # }

# def bootstrap(theta, n, delta_target, q, b):
#     """
#     Bootstrap subroutine for computing the accuracy of a given n value, incorporating
#     delta_target to adjust for the target confidence level.
#
#     :param theta: The distribution (array) from which to sample.
#     :param n: The sample size.
#     :param delta_target: The target confidence level, used to calculate the specific epsilon.
#     :param q: The quantile to compute.
#     :param b: The number of resampling iterations.
#     :return: The computed accuracy epsilon at the specified quantile and confidence level.
#     """
#     theta = np.asarray(theta).flatten()
#
#     if len(theta) == 0:
#         raise ValueError("Input data (theta) is empty.")
#     if n <= 0 or not isinstance(n, int):
#         raise ValueError("Sample size (n) must be a positive integer.")
#     if n > len(theta):
#         n = len(theta)  # Adjust n to the maximum allowable size
#
#     # Sample S0 from theta
#     S_0 = np.random.choice(theta, size=n, replace=True)
#     x_0 = np.quantile(S_0, q)
#
#     epsilons = []
#     for _ in range(b):
#         S_i = np.random.choice(S_0, size=n, replace=True)
#         x_i = np.quantile(S_i, q)
#         epsilons.append(abs(x_i - x_0))
#
#     epsilons.sort()
#
#     # Correct calculation of s_index based on the given formula
#     s_index = int(1 + b * (delta_target / 2))
#     # Ensure s_index does not exceed the bounds of epsilons
#     s_index = min(max(s_index, 1), len(epsilons)) - 1
#
#     # Select epsilon at index s as the accuracy measure
#     epsilon_s = epsilons[s_index]
#
#     # Given the potential for always returning 0, let's ensure variability
#     # by checking if the epsilon_s is 0 and adjusting the logic slightly
#     if epsilon_s == 0 and len(epsilons) > 1:
#         # Consider the next non-zero epsilon in the sorted list as a fallback
#         non_zero_epsilons = [e for e in epsilons if e > 0]
#         if non_zero_epsilons:
#             epsilon_s = non_zero_epsilons[0]  # Smallest non-zero epsilon
#         else:
#             # In the unlikely case all epsilons are 0, return the smallest non-zero float
#             epsilon_s = np.finfo(float).eps
#
#     return epsilon_s



# import numpy as np
#
# def bootstrap(theta, n, delta_target, q, b):
#     """
#     Bootstrap subroutine for computing the accuracy of a given n value, incorporating
#     delta_target to adjust for the target confidence level.
#
#     :param theta: The distribution (array) from which to sample.
#     :param n: The sample size.
#     :param delta_target: The target confidence level, used to calculate the specific epsilon.
#     :param q: The quantile to compute.
#     :param b: The number of resampling iterations.
#     :return: The computed accuracy epsilon at the specified quantile and confidence level.
#     """
#     theta = np.asarray(theta).flatten()
#
#     if len(theta) == 0:
#         raise ValueError("Input data (theta) is empty.")
#
#     if n <= 0 or not isinstance(n, int):
#         raise ValueError("Sample size (n) must be a positive integer.")
#
#     if n > len(theta):
#         n = len(theta)  # Adjust n to the maximum allowable size
#
#     # Sample S0 from theta
#     S_0 = np.random.choice(theta, size=n, replace=True)
#     x_0 = np.quantile(S_0, q)
#
#     epsilons = []
#     for _ in range(b):
#         S_i = np.random.choice(S_0, size=n, replace=True)
#         x_i = np.quantile(S_i, q)
#         epsilons.append(abs(x_i - x_0))
#         # print(f"epsilons: {epsilons}")
#
#     epsilons.sort()
#     # Calculate s using the formula s = 1 + b * (delta_target / 2)
#     s_index = int(1 + b * (delta_target / 2))
#     # Ensure s_index does not exceed the bounds of epsilons
#     s_index = min(max(s_index, 1), len(epsilons)) - 1  # Adjust index for 0-based indexing
#
#     # Select epsilon at index s as the accuracy measure
#     epsilon_s = epsilons[s_index]
#
#     return epsilon_s


# import numpy as np
#
# def bootstrap(theta, n, delta_target, q, b):
#     """
#     Updated bootstrap subroutine for computing the accuracy of a given n value, incorporating
#     delta_target in the statistical smoothing process.
#
#     :param theta: The distribution (array) from which to sample.
#     :param n: The sample size.
#     :param delta_target: The target confidence level, used to adjust smoothing.
#     :param q: The quantile to compute, with a slight adjustment for robustness.
#     :param b: The number of resampling iterations for smoothing.
#     :return: The computed accuracy epsilon, after applying statistical smoothing and considering delta_target.
#     """
#     theta = np.asarray(theta).flatten()
#
#     if len(theta) == 0:
#         raise ValueError("Input data (theta) is empty.")
#
#     if n <= 0 or not isinstance(n, int):
#         raise ValueError("Sample size (n) must be a positive integer.")
#
#     if n > len(theta):
#         n = len(theta)  # Adjust n to the maximum allowable size
#
#     S_0 = np.random.choice(theta, size=n, replace=True)
#     # Adjust the quantile slightly if needed to be more robust
#     adjusted_q = q + 0.05 if q + 0.05 <= 1 else q - 0.05
#     x_0 = np.quantile(S_0, adjusted_q)
#
#     epsilons = []
#     for _ in range(b):
#         S_i = np.random.choice(S_0, size=n, replace=True)
#         x_i = np.quantile(S_i, adjusted_q)
#         epsilon = abs(x_i - x_0)
#         epsilons.append(epsilon)
#
#     # # Apply statistical smoothing to the calculated epsilons, influenced by delta_target
#     # # The idea here is to use delta_target to adjust how much we rely on the extremes of the epsilon values
#     # # For higher confidence (lower delta_target), we might want to be more conservative with our epsilon estimate
#     # smoothing_factor = max(1 - delta_target, 0.1)  # Ensure smoothing factor is not too low; adjust as needed
#     # sorted_epsilons = sorted(epsilons)
#     # smoothed_epsilon = np.mean(sorted_epsilons[int(b*smoothing_factor*0.5):-int(b*smoothing_factor*0.5)])
#     #
#     #
#
#     return smoothed_epsilon
