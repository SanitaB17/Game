# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

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


def main_menu():
    # ASCII art title
    title = """
,------.                  ,--.      ,--------.             ,--.         
|  .--. ' ,---. ,--,--, ,-'  '-.    '--.  .--',---.  ,---. |  | ,--,--. 
|  '--'.'| .-. :|      \\'-.  .-'       |  |  | .-. :(  .-' |  |' ,-.  | 
|  |\\  \\ \\   --.|  ||  |  |  |         |  |  \\   --..-'  `)|  |\\ '-'  | 
`--' '--' `----'`--''--'  `--'         `--'   `----'`----' `--' `--`--' 
                ,----.     ,--.   ,--.     ,---.                        
                '.-.  |     \  `.'  /     '   .-'                       
                  .' <       '.    /      `.  `-.                       
                /'-'  |        |  |       .-'    |                      
                `----'         `--'       `-----'                       
    """
    # Main menu options
    menu_options = [
        "1. Rent Car",
        "2. View Booking",
        "3. Cancel Booking"
    ]

    # Display the ASCII art title
    print(title)

    # Display the main menu options
    for option in menu_options:
        print(option)

    # Get user input for menu selection
    choice = input("Please enter your choice: ")

    if choice == "1":
        print("You chose Option Rent Car")
    elif choice == "2":
        print("You chose View Booking")
    elif choice == "3":
        print("You chose Cancel Booking")
        return
    else:
        print("Invalid choice. Please try again.")

    # Recursive call to display the main menu again
    main_menu()


# Call the main menu function to start the program
main_menu()