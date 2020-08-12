initial_amount = 100
interest_rate = 5.0
num_of_years = 0

for num_of_years in range(11):
    final_amount = initial_amount * (1 + interest_rate/100) ** num_of_years
    print(f"Year: {num_of_years}\tInitial Amount: {initial_amount}\tFinal Amount: {final_amount}")