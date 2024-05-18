import mpmath

# Define the number of decimal places for the calculations
mpmath.mp.dps = 50

# Set the range to check
start_range = 1
end_range = 1000

# Define the zeta function
zeta = mpmath.zetazero

# Check if the real part of all non-trivial zeros is 0.5 (as per the Riemann Hypothesis)
for n in range(start_range, end_range + 1):
    zero = zeta(n)
    if mpmath.nstr(mpmath.re(zero), 3) != '0.5':
        print(f"The Riemann Hypothesis does not hold true for n = {n}")
        break
else:
    print(f"The Riemann Hypothesis holds true for all n from {start_range} to {end_range}")
