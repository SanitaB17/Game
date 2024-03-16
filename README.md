# Tesla

**Tesla** is a CLI data automation program created for educational purposes only as part of the [Code Institute](https://codeinstitute.net/ie/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI%2B-%2BIRL%2B-%2BSearch%2B-%2BBrand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14304747355&hsa_grp=128775288209&hsa_ad=635725005315&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwwMqvBhCtARIsAIXsZpZC495GdKzsmvgCTZoifPZGwIm_vcoRPwF45OvGEB0qwplfPY2MoZUaAk_MEALw_wcB) Diploma in Full-Stack Software Development.

[Live Preview of Tesla](https://rent-tesla-fbe3f5ee7ebb.herokuapp.com/)

![Main view](docs/images/main-view.JPG)


## Table of Contents

- [Tesla](#tesla)
  - [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [User](#user)
  - [User Goals](#user-goals)
  - [User Story](#user-story)
  - [Site owners Goals](#site-owners-goals)
  - [Program flowchart](#program-flowchart)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Technology used](#technology-used)


# UX

## User

## User Goals

- Rent Tesla car.
- View Booking.
- Cancel booking.

## User Story

- As a  user, I want to be able to rent a Tesla car so that I can use it for my transportation needs.
- As a  user, I want to view my booking details so that I can verify the information.
- As a  user,  I want to cancel my booking if my plans change so that I can avoid unnecessary charges and free up the car for other customers.

## Site owners Goals

- Easy to navigate.
- Provide a diverse selection of Tesla car models and prices.
- Provide feedback or a response to the user when they perform a task or action.
- Implement a reservation system to allow users to schedule car rentals in advance, ensuring availability and convenience.

## Program flowchart

During planning, I created a flowchart of how I wanted program to work and interact. The flowchart was created using [Figma](https://www.figma.com/)

![Flow-chart](docs/images/flow-chart.JPG)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Features

## Existing Features

- The Main Menu:
  - Users are greeted and presented with three options to choose from.

![Main](docs/images/main.JPG)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

- Rent Car Section:
  - This section allows users to input their desired rental dates (present and future dates) and choose a car model. It also provides feedback if a car is unavailable during those dates. 

![Selected Car Unavailable](docs/images/car-unavailable-display.JPG)

  - Displays a summary of booking details and cost.

![Rent Car Section](docs/images/rent-car-section.JPG)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

- View Booking:
  - This section allows users to search for their booking by entering their name. If the user has booked a car, it will display all information regarding the user's booking.
  
![View Booking](docs/images/view-booking.JPG)

  - If no booking is found for the entered name, it will inform the user accordingly.

![Booking Not Found](docs/images/booking-not-found.JPG)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

- Cancel Booking:
  - In this section, users are provided with the option to cancel their booking. Users will be prompted to input their name to identify their booking. If a booking is found for the entered name, the system will display all relevant booking information and prompt the user to confirm the cancellation. If confirmed, the booking will be canceled.
  
![Cancel Booking](docs/images/cancel-b.JPG)

  - If no booking is found for the entered name, user will be informed accordingly.

![Cancel Booking Not Found](docs/images/cancel-b-not-f.JPG)

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Future Features

- Generate Booking IDs:
  -  When a user makes a booking, generate a unique booking ID for that reservation.
 
# Technology used

- **[HTML](https://www.youtube.com/watch?v=3OTSsq9Y0P4&t=5s)**
- **[CSS](https://www.youtube.com/watch?v=nV9oaUglBTE)**
- **[JavaScript](https://www.youtube.com/watch?v=wm4F0Zqxu5A)**
- **[Python](https://www.youtube.com/watch?v=vRsFb4nMGP4)** Was used to create the program.
- **[os Module](https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)** Used for clearing the terminal.
- **[tabulate Module](https://360digitmg.com/blog/python-tabulate)** Used to present data in a table format.
- **[datetime Module](https://www.programiz.com/python-programming/datetime)** Used for handling date and time operations.
- **[VSCode](https://en.wikipedia.org/wiki/Visual_Studio_Code)** Was used to write code.
- **[Google Sheets](https://en.wikipedia.org/wiki/Google_Sheets)** Was used to store data.
- **[gspread](https://github.com/burnash/gspread)** Was used to allow the Python program to interact with Google Sheets.
- **[google.oauth2.service_account Credentials](https://google-auth.readthedocs.io/en/latest/reference/google.oauth2.service_account.html#google.oauth2.service_account.Credentials)**: Used for authentication with Google APIs using service account credentials.
- **[Heroku](https://www.heroku.com/)** Was used to deploy the project.
- **[GitHub](https://en.wikipedia.org/wiki/GitHub)** Version control and repository hosting.
- **[Git](https://en.wikipedia.org/wiki/Git)** - Version control system used to commit and push code during development.
- **[Figma](https://www.figma.com/)** - Used to create the flowchart.
- **[pep8ci](https://pep8ci.herokuapp.com/)** Used to check python code for errors.

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;