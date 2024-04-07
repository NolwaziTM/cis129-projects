def check_protect(amount):
    # Convert the amount to a string and strip any leading or trailing whitespace
    amount_str = str(amount).strip()

    # Check if the amount has a decimal point
    if '.' in amount_str:
        dollars, cents = amount_str.split('.')
    else:
        dollars = amount_str
        cents = '00'

    # Calculate the number of leading asterisks needed
    num_asterisks = 10 - len(dollars) - len(cents) - 1  # Subtracting 1 for the decimal point

    # Create the check-protected format
    protected_amount = '*' * num_asterisks + dollars + '.' + cents

    return protected_amount


# Test the function
amount = float(input("Enter the dollar amount: "))
protected_amount = check_protect(amount)
print("Check-protected amount:", protected_amount)
