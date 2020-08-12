num_of_years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_of_years.append(10)

initial_amount = 100
interest_rate = 5.0

for n in num_of_years:
    final_amount = initial_amount * (1 + interest_rate/100) ** n
    print(f"Year: {n}\tInitial Amount: {initial_amount}\tFinal Amount: {final_amount}")