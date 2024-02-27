# Module 05 - Lab 5
# Title: The Bottle Return Program
# Author : Nolwazi Moyo
# Date: 02/26/2024

# Step 1: Declare variables 
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = "y"


def get_bottles():
    NBR_OF_DAYS = 7
    today_bottles = 0
    counter = 1

    while counter <= NBR_OF_DAYS:
        today_bottles = int(input("Enter number of bottles returned for day #" + str(counter) + ": "))
        total_bottles += today_bottles
        counter += 1


    return total_bottles


def calc_payout(total_bottles):
    PAYOUT_PER_BOTTLE = 0.10
    return total_bottles * PAYOUT_PER_BOTTLE

def print_info(total_bottles, total_payout):
    print("Total number of bottles collected: ", total_bottles)
    print("Total payout: $", total_payout) 

#step 2: loop to run program again
while keep_going.lower() == "y":
    #code to set value of variables
    total_bottles = get_bottles()
    total_payout = calc_payout(total_bottles)
    print_info(total_bottles, total_payout)

    keep_going = input("Do you want to enter another week's worth of data? (Enter y or n ): ")

