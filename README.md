# 📊 Comparison of Option Pricing Techniques

This project explores and compares two fundamental models used in **European option pricing** — the **Binomial Tree Model** and the **Black-Scholes Model**.  
It aims to evaluate their **accuracy, efficiency, and applicability** under different market conditions using **Python simulations**.

---

## 🧮 Project Overview

The valuation of financial derivatives plays a crucial role in global markets.  
European options, which can only be exercised at maturity, are priced using mathematical models that consider market volatility, risk-free rates, and time to expiration.

This project focuses on:
- Deriving and implementing the **Binomial Tree Model** and **Black-Scholes Model**
- Comparing their **results**, **sensitivity to volatility**, and **computational efficiency**
- Discussing their strengths, weaknesses, and real-world applicability

---

## 📁 Repository Structure

Comparison-of-Option-Pricing-Techniques/

 - 📄 binomial_tree_model.py # Python implementation of Binomial Tree Model
 - 📄 black_scholes_model.py # Python implementation of Black-Scholes Model
 - 📄 results_comparison.ipynb # Notebook comparing both models
 - 📄 README.md # Project documentation (this file)
 - 📄 MAT322_Project_Report.pdf # Full academic report



---

## ⚙️ Requirements

To run this project, you need:

- Python 3.8+
- NumPy
- Matplotlib (optional, for visualizations)
- Jupyter Notebook (optional, for running the simulation interactively)

You can install dependencies with:

```bash
pip install numpy matplotlib
🚀 Running the Code
🧩 Binomial Tree Model
bash
Copy code
python binomial_tree_model.py
🧠 Black-Scholes Model
bash
Copy code
python black_scholes_model.py
Both scripts display the European Call and Put Option Prices based on given input parameters.

📊 Results Summary
Model	Call Option (₵)	Put Option (₵)	Notes
Binomial Tree	652.29	499.23	Accurate under low volatility, requires many steps for precision
Black-Scholes	651.19	498.13	Stable and efficient under all volatility levels

📈 Both models yield comparable results, but differ in computational methods:

Binomial Model: Discrete, step-based, more flexible but slower.

Black-Scholes Model: Continuous-time, closed-form, fast but assumes constant volatility.

💬 Discussion
The Binomial Tree Model becomes computationally expensive as the number of steps increases, but it can handle more complex scenarios (e.g., American options).

The Black-Scholes Model is elegant and efficient but relies on assumptions (constant volatility, no dividends, lognormal asset price).

Under South African market conditions, both models remain valid, but Black-Scholes performs better for high-volatility assets.

🧠 Key Concepts Covered
Geometric Brownian Motion (GBM)

Risk-neutral valuation

Cumulative Normal Distribution (Φ)

Put-Call Parity

Sensitivity (Ω – Omega)

Monte Carlo concepts (for potential extension)

🧾 References
F. Black and M. Scholes. The Pricing of Options and Corporate Liabilities. Journal of Political Economy, 81(3):637–654, 1973.

K. Riaman et al. Convergence of Binomial Tree Methods to Black-Scholes Model on Determining Stock Option Prices. IOP Conf. Series, 2019.

S. Shao. Pricing Technique for European Option and Application. Highlights in Business, Economics, and Management, 2023.

S.M. Ross. Mathematical Finance. Cambridge University Press, 2011.

👩🏽‍💻 Authors
Group 5 — MAT322 Research Project

Kgosietsile Thuso Ntsono

Nathanial Petersen

Shumani Raludzingana

Yamkelani Socamangashe

🌟 Acknowledgements
Special thanks to the University of Western cape and the MAT322 course team for their guidance and resources.

📌 Future Work
Extend to American Options

Include Monte Carlo Simulation for exotic options

Visualize option price convergence vs. number of steps or volatility

🏷️ License
This project is open-source under the MIT License.
