import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tesla')

sales = SHEET.worksheet('bookings')

# Global variable for car availability
AVAILABLE = {
    'Tesla model 3': 1,
    'Tesla model Y': 2,
    'Tesla model S': 1
}

# Global variable for car rental prices
PRICE_PER_DAY = {
    'Tesla model 3': 50,
    'Tesla model Y': 70,
    'Tesla model S': 75
}


def main_menu():
    """
    Welcome message and main menu
    """
    print("\n###############################################")
    print("Welcome to the Tesla car rental system")
    print("###############################################\n")
    print("Please select an option from the main menu\n")
    print("1. Rent Car")
    print("2. View Booking")
    print("3. Cancel Booking\n")

    while True:
        try:
            choice = int(input("Please Enter your choice: "))
            if choice not in range(1, 4):
                raise ValueError("Please enter a number between 1 and 3.")
            break
        except ValueError as ve:
            print(ve)
            continue

    if choice == 1:
        rent_car()
    elif choice == 2:
        view_booking()
    elif choice == 3:
        cancel_booking()


def rent_car():
    """
    Rent Car function to select car and add to booking
    """
    cars = list(AVAILABLE.keys())

    while True:
        st_d_str = input("Enter start date (DD-MM-YYYY): ")
        end_d_str = input("Enter end date (DD-MM-YYYY): ")
        try:
            st_d = datetime.strptime(st_d_str, '%d-%m-%Y')
            end_d = datetime.strptime(end_d_str, '%d-%m-%Y')
            if st_d >= end_d:
                raise ValueError("End date should be after start date.")
        except ValueError as ve:
            print(ve)
            continue

        if not any(a_car_available(car, st_d, end_d) for car in cars):
            print("Sorry, no cars available for rent at the specified dates.")
            while True:
                choice = input("Select model or exit? (return/exit): ").lower()
                if choice == "return":
                    break
                elif choice == "exit":
                    main_menu()
                else:
                    print("Invalid choice. Please enter 'return' or 'exit'.")
                    continue
            continue

        print("Please select a car model to rent\n")
        for i, car in enumerate(cars, start=1):
            print(f"{i}. {car}")

        while True:
            try:
                choice = int(input("Please select a car model to rent: "))
                if choice not in range(1, len(cars) + 1):
                    raise ValueError("Please select a valid car number.")
                car = cars[choice - 1]
                if not a_car_available(car, st_d, end_d):
                    raise ValueError(f"Sorry, {car} is fully booked.")
                break
            except ValueError as ve:
                print(ve)
                continue

        break

    user_n = input("Please enter your name: ")
    while not user_n.isalpha():
        print("Name should contain only letters.")
        user_n = input("Please enter your name: ")

    days = (end_d - st_d).days
    tot_p = booking_cost(car, days)
    print(f"\nYou have selected to rent the {car} for {days} days")
    print(f"Rental period: {st_d_str} to {end_d_str}")
    print(f"User name: {user_n}")
    print(f"Total price: ${tot_p}")

    while True:
        confirm = input("Please confirm your booking (yes/no): ").lower()
        if confirm == "yes":
            sales.append_row([user_n, car, st_d_str, end_d_str, days, tot_p])
            print("Booking confirmed!")
            print("Thank you for using our service!")
            break
        elif confirm == "no":
            print("Booking cancelled!")
            break
        else:
            print("Please enter 'yes' or 'no'")
    print("Returning to main menu...")
    main_menu()


def a_car_available(car, start_date, end_date):
    """
    Checks if a specific car is available for the specified dates
    """
    bookings = sales.get_all_values()
    for booking in bookings:
        if booking[1] == car:
            booking_st = datetime.strptime(booking[2], '%d-%m-%Y')
            booking_end = datetime.strptime(booking[3], '%d-%m-%Y')
            if (start_date >= booking_st and start_date <= booking_end) or \
               (end_date >= booking_st and end_date <= booking_end):
                return False
    return True


def booking_cost(car, days):
    """
    Calculates total price for the car rental
    """
    return PRICE_PER_DAY[car] * days


def view_booking():
    """
    Search for a name and prints the booking details
    """
    search_n = input("Please enter your name: ")

    bookings = sales.get_all_values()

    m_bookings = [booking for booking in bookings if booking[0] == search_n]

    if not m_bookings:
        print(f"No bookings found for {search_n}")
    else:
        print("Bookings found:")
        for booking in m_bookings:
            print(booking)


main_menu()
