# Define tax brackets and rates
tax_brackets = [
    (10000, 0.1),   # 10% for income up to $10,000
    (30000, 0.2),   # 20% for income up to $30,000
    (50000, 0.25),  # 25% for income up to $50,000
    (float('inf'), 0.3)  # 30% for income above $50,000
]

# Define location-specific rent-to-income ratios
location_ratios = {
    'cityA': 0.25,
    'cityB': 0.30,
    'cityC': 0.35
}

# Define housing policies affecting maximum allowable rent
housing_policies = {
    'policy1': 1000,
    'policy2': 1200,
    'policy3': 1500
}

def calculate_tax(yearly_income):
    tax = 0
    remaining_income = yearly_income
    for bracket, rate in tax_brackets:
        if remaining_income > bracket:
            tax += bracket * rate
            remaining_income -= bracket
        else:
            tax += remaining_income * rate
            break
    return tax

def calculate_rent_eligibility(yearly_income, location, housing_policy):
    # Calculate post-tax income
    tax = calculate_tax(yearly_income)
    post_tax_income = yearly_income - tax

    # Get the rent-to-income ratio for the location
    if location in location_ratios:
        ratio = location_ratios[location]
    else:
        print("Location not found. Using default ratio of 0.30.")
        ratio = 0.30

    # Calculate maximum rent based on post-tax income
    max_rent_based_on_income = post_tax_income * ratio

    # Get the housing policy limit
    if housing_policy in housing_policies:
        policy_limit = housing_policies[housing_policy]
    else:
        print("Housing policy not found. Using default policy limit of $1000.")
        policy_limit = 1000

    # Final eligible rent is the minimum of the two calculated values
    eligible_rent = min(max_rent_based_on_income, policy_limit)
    return eligible_rent

def main():
    # Get user input for yearly income, location, and housing policy
    try:
        yearly_income = float(input("Enter your yearly income: "))
        location = input("Enter your location (cityA, cityB, cityC): ")
        housing_policy = input("Enter your housing policy (policy1, policy2, policy3): ")
    except ValueError:
        print("Invalid input. Please enter valid values.")
        return

    # Calculate rent eligibility
    eligible_rent = calculate_rent_eligibility(yearly_income, location, housing_policy)
    print(f"You are eligible for a maximum rent of ${eligible_rent:.2f}")

if __name__ == "__main__":
    main()
