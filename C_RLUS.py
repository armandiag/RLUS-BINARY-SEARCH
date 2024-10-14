import numpy as np
from C_bootstrap import bootstrap

def set_rho(q, delta_target, epsilon_range, theta, b):
    UB = len(theta)
    LB = 1
    final_rho = None
    epsilon_min, epsilon_max = epsilon_range

    while LB <= UB:
        n = (UB + LB) / 2  # Ensure n is always a positive integer
        print(f"-------------------")
        print(f"LB: {LB}, UB: {UB}, n: {n}")

        current_epsilon = bootstrap(theta, n, delta_target, q, b)
        print(f"E_i: {current_epsilon}")

        if epsilon_min <= current_epsilon <= epsilon_max:
            final_rho = n
            print(f"epsilon_min: {epsilon_min}, epsilon_max: {epsilon_max}")
            print(f"final_rho: {final_rho}")
            break
        elif current_epsilon < epsilon_min:
            LB = n + 1
            print(f"epsilon_min: {epsilon_min}, epsilon_max: {epsilon_max}")
            print(f"current_epsilon < epsilon_min, updating LB to {LB}")
        else:  # current_epsilon > epsilon_max
            UB = n - 1
            print(f"epsilon_min: {epsilon_min}, epsilon_max: {epsilon_max}")
            print(f"current_epsilon > epsilon_max, updating UB to {UB}")

    return final_rho
