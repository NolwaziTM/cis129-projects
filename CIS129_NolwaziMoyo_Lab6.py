# Module 06 : Lab 06
# Title : Hotdog Cookout Lab
# Author : Nolwazi Moyo
# Date : 03/04/2024


def getTotalHotDogs():
    attendees = int(input("Enter the number of people attending the cookout: "))
    hotDogs = int(input("Enter the number of hot dogs each person will be given: "))
    total = attendees * hotDogs
    return total

def showResults(total):
    DOGS = 10
    BUNS = 8
    dogsLeft = (DOGS - total % DOGS) % DOGS
    minDogs = (total // DOGS) + (0 ** (0 ** dogsLeft))
    bunsLeft = (BUNS - total % BUNS) % BUNS
    minBuns = (total // BUNS) + (0 ** (0 ** bunsLeft))
    
    print("Minimum packages of hot dogs needed:", minDogs)
    print("Minimum packages of hot dog buns needed:", minBuns)
    print("Hot dogs remaining:", dogsLeft)
    print("Hot dog buns remaining:", bunsLeft)

def main():
    totalHotDogs = getTotalHotDogs()
    showResults(totalHotDogs)

if __name__ == "__main__":
    main()
