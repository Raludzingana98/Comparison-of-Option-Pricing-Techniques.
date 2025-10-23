import math

# -------------------------------
# PARAMETERS
# -------------------------------
S0 = 15600     # Initial stock price
K = 15700      # Strike price
T = 0.25       # Time to maturity (in years)
sigma = 0.1846 # Volatility
r = 0.065      # Risk-free interest rate
n = 100        # Number of steps in the binomial tree

# -------------------------------
# STEP 1: CALCULATE MODEL FACTORS
# -------------------------------
dt = T / n                      # Length of each time step
u = math.exp(sigma * math.sqrt(dt))  # Upward movement factor
d = math.exp(-sigma * math.sqrt(dt)) # Downward movement factor
p = (math.exp(r * dt) - d) / (u - d) # Risk-neutral probability
beta = math.exp(-r * dt)             # Discount factor

# -------------------------------
# STEP 2: CALCULATE STOCK PRICES AT MATURITY
# -------------------------------
stock_prices = [S0 * (u ** (n - i)) * (d ** i) for i in range(n + 1)]

# -------------------------------
# STEP 3: CALCULATE OPTION VALUES AT MATURITY
# -------------------------------
call_values = [max(price - K, 0) for price in stock_prices]
put_values = [max(K - price, 0) for price in stock_prices]

# -------------------------------
# STEP 4: BACKWARD INDUCTION
# -------------------------------
# Compute option values at earlier nodes by working backwards
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        call_values[j] = beta * (p * call_values[j] + (1 - p) * call_values[j + 1])
        put_values[j] = beta * (p * put_values[j] + (1 - p) * put_values[j + 1])

# -------------------------------
# STEP 5: OUTPUT FINAL OPTION PRICES
# -------------------------------
call_price = call_values[0]
put_price = put_values[0]

print("----------------------------------------------------")
print(" European Option Pricing using Binomial Tree Model ")
print("----------------------------------------------------")
print(f"Initial Stock Price (S0): {S0}")
print(f"Strike Price (K): {K}")
print(f"Time to Maturity (T): {T} years")
print(f"Volatility (sigma): {sigma}")
print(f"Risk-Free Rate (r): {r}")
print(f"Number of Steps (n): {n}")
print("----------------------------------------------------")
print(f"European Call Option Price: {call_price:.4f}")
print(f"European Put  Option Price: {put_price:.4f}")
print("----------------------------------------------------")
