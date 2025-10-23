import numpy as np

# ---------------------------------------------------
# PARAMETERS
# ---------------------------------------------------
S0 = 15675     # Initial stock price
K = 500        # Strike price
T = 0.25       # Time to maturity (in years)
r = 0.065      # Risk-free interest rate
sigma = 0.1846 # Volatility

# ---------------------------------------------------
# FUNCTION: Cumulative Distribution Function (Φ)
# ---------------------------------------------------
def phi(x):
    """
    Approximation of the standard normal cumulative distribution function (Φ).
    """
    a1 = 0.319381530
    a2 = -0.356563782
    a3 = 1.781477937
    a4 = -1.821255978
    a5 = 1.330274429

    if x >= 0:
        y = 1 / (1 + 0.2316419 * x)
        return 1 - (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2) * \
            (a1 * y + a2 * y**2 + a3 * y**3 + a4 * y**4 + a5 * y**5)
    else:
        return 1 - phi(-x)

# ---------------------------------------------------
# STEP 1: COMPUTE OMEGA (ω)
# ---------------------------------------------------
omega = (r * T + (sigma**2 * T) / 2 - np.log(K / S0)) / (sigma * np.sqrt(T))

# ---------------------------------------------------
# STEP 2: BLACK-SCHOLES FORMULAS
# ---------------------------------------------------
# European Call Option Price
C = S0 * phi(omega) - K * np.exp(-r * T) * phi(omega - sigma * np.sqrt(T))

# European Put Option Price (from Put-Call Parity)
P = C + K * np.exp(-r * T) - S0

# ---------------------------------------------------
# STEP 3: OUTPUT RESULTS
# ---------------------------------------------------
print("----------------------------------------------------")
print(" European Option Pricing using Black-Scholes Model ")
print("----------------------------------------------------")
print(f"Initial Stock Price (S0): {S0}")
print(f"Strike Price (K): {K}")
print(f"Time to Maturity (T): {T} years")
print(f"Volatility (sigma): {sigma}")
print(f"Risk-Free Rate (r): {r}")
print("----------------------------------------------------")
print(f"Omega (ω): {omega:.6f}")
print(f"European Call Option Price: {C:.4f}")
print(f"European Put  Option Price: {P:.4f}")
print("----------------------------------------------------")
