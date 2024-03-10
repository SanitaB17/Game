# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
import os
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

data = sales.get_all_values()

PRICE_PER_DAY = {
    'Tesla model 3': 50,
    'Tesla model Y': 70,
    'Tesla model S': 75
}


def main_menu():
    """
    Welcome message and main menu
    """
    os.system("clear")
    print("###############################################")
    print("Welcome to the Tesla car rental system")
    print("###############################################")
    print("Please select an option from the main menu")
    print("1. Rent Car")
    print("2. View Booking")
    print("3. Cancel Booking")
    while True:
        try:
            choice = int(input("Please Enter your choice: \n"))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if choice == 1:
            rent_car()
        elif choice == 2:
            view_booking()
        elif choice == 3:
            cancel_booking()
            break
        else:
            print("Please select a number between 1 and 3\n")


def rent_car():
    """
    Rent Car function to select car and add to booking
    """
    os.system("clear")
    print("Please select a car model to rent")
    print("")
    print("1. Tesla model 3")
    print("2. Tesla model Y")
    print("3. Tesla model S")
    print("")

    while True:
        choice = input("Please select a car model to rent: \n")
        if choice == "1":
            car = "Tesla model 3"
            break
        elif choice == "2":
            car = "Tesla model Y"
            break
        elif choice == "3":
            car = "Tesla model S"
            break
        else:
            print("Please select a number between 1 and 3\n")

    while True:
        user_n = input("Please enter your name: ")
        if not user_n.isalpha():
            print("Name should contain only letters.")
            continue
        break

    while True:
        try:
            start_d_str = input("Enter start date (DD-MM-YYYY): ")
            start_d = datetime.strptime(start_d_str, '%d-%m-%Y')
            end_d_str = input("Enter end date (DD-MM-YYYY): ")
            end_d = datetime.strptime(end_d_str, '%d-%m-%Y')
            days = (end_d - start_d).days
            if days < 0:
                raise ValueError("End date should be after start date.")
            break
        except ValueError as ve:
            print(ve)
            continue
    tot = booking_cost(car, days)
    print(f"You have selected to rent the {car} for {days} days")
    print(f"Rental period: {start_d_str} to {end_d_str}")
    print(f"User name: {user_n}")
    print(f"Total price: ${tot}")

    while True:
        confirm = input("Please confirm your booking (yes/no): \n")
        if confirm.lower() == "yes":
            """
            Store details in Google Sheet
            """
            sales = SHEET.worksheet('bookings')
            sales.append_row([user_n, car, start_d_str, end_d_str, days, tot])
            print("Booking confirmed!")
            break
        elif confirm.lower() == "no":
            print("Booking cancelled!")
            break
        else:
            print("Please enter 'yes' or 'no'\n")
    main_menu()


def booking_cost(car, days):
    """
    Calculates total price for the car rental
    """
    cost_per_day = PRICE_PER_DAY[car]
    tot = cost_per_day * days
    return tot


main_menu()
