# Module 7: Lab 07
# Title : Theater Seating Lab
# Author : Nolwazi Moyo
# Date : 03/11/2024

# Constants
SECTIONS = ['A', 'B', 'C']  # Section names
SEAT_PRICES = {'A': 20, 'B': 15, 'C': 10}  # Price per seat for each section
SEAT_COUNTS = {'A': 300, 'B': 500, 'C': 200}  # Number of seats in each section

def display_constants():
    """Display welcome message with constant values."""
    print("Welcome to the theater ticket sales program!")
    print("Section Names:", SECTIONS)
    print("Seat Prices:", SEAT_PRICES)
    print("Seat Counts:", SEAT_COUNTS)
    print()

def get_ticket_sales():
    """Get number of tickets sold in each section."""
    ticket_sales = {}
    for section in SECTIONS:
        while True:
            try:
                num_tickets = int(input(f"Enter the number of tickets sold for section {section}: "))
                if num_tickets < 0:
                    print("Please enter a positive number.")
                elif num_tickets > SEAT_COUNTS[section]:
                    print("Not enough seats available in this section.")
                else:
                    ticket_sales[section] = num_tickets
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return ticket_sales

def calculate_income(ticket_sales):
    """Calculate income generated from ticket sales."""
    total_income = 0
    for section, num_tickets in ticket_sales.items():
        price_per_seat = SEAT_PRICES[section]
        section_income = num_tickets * price_per_seat
        total_income += section_income
        print(f"Subtotal for Section {section}: ${section_income}")
    print("Overall Total Income: $", total_income)

def main():
    display_constants()
    ticket_sales = get_ticket_sales()
    calculate_income(ticket_sales)

if __name__ == "__main__":
    main()
