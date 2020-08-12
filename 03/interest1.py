initial_amount = 100
interest_rate = 5.0
num_of_years = 0

# The while-loop runs until the conditional-statement evaluates to false.
while num_of_years <= 10:
    final_amount = initial_amount * (1 + interest_rate/100) ** num_of_years
    print(f"\tYear: {num_of_years}\tInitial Amount: {initial_amount}\tFinal Amount: {final_amount}")
    num_of_years = num_of_years + 1