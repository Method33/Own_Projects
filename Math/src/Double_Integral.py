from scipy import integrate

# Get user inputs
print("Enter the function of two variables to integrate (e.g., 'x*y'). The variables are 'x' and 'y': ")
user_func = input()

print("Enter the lower limit for x: ")
x_lower = float(input())

print("Enter the upper limit for x: ")
x_upper = float(input())

print("Enter the lower limit for y: ")
y_lower = float(input())

print("Enter the upper limit for y: ")
y_upper = float(input())

# Define the user's function
def f(x, y):
    return eval(user_func)

# Calculate the double integral
result, error = integrate.dblquad(f, x_lower, x_upper, lambda x : y_lower, lambda x: y_upper)

print(f"The result of the double integral is: {result}")
