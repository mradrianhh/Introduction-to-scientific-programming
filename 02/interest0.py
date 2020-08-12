# Variables can be used to hold information.

# Integer-type
initial_amount = 100

# Float-type
interest_rate = 5.0

# Integer-type
num_of_years = 7

# The type of "final_amount" must be deduced from the number-types in the expression.
# The type of "final_amount" will be the least precise type that's involved in the calculation.
# Thus, the type will be a float in this scenario.
# I.e: if you were to multiply two integers, the result would be an integer.
final_amount = initial_amount * (1+interest_rate/100)**num_of_years

print(f"After {num_of_years} years, {initial_amount} has grown to {final_amount:.2f}.")