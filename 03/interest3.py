initial_amount = 100
interest_rate_high = 5.0
interest_rate_low = 2.5

num_of_years = 10

final_amount_high = []
final_amount_low = []

for n in range(num_of_years + 1):
    final_amount_high.append(initial_amount * (1 + interest_rate_high/100) ** n)
    final_amount_low.append(initial_amount * (1 + interest_rate_low/100) ** n)

for low, high in zip(final_amount_low, final_amount_high):
    print(f"Low: {low:.2f}\tHigh: {high:.2f}")