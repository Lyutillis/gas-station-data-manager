# gas-station-data-manager

This app was created to help Gas Station owners manage their revenues, and related data, such as fuel types and price and discounts.

To launch the application, follow next steps:

1. Fork the repository

2. Clone it to your device:
`git clone <here goes the HTTPS link you could copy on github repositiry page>`

3. Create virtual environment:
`python3 -m venv venv`

4. Install requirements:
`pip3 install -r requirements.txt`

5. Run migrations:
`python3 manage.py migrate`

6. Load the data from fixture:
`python3 manage.py loaddata fixtures/db_data.json`

7. Run server:
`python3 manage.py runserver`

To run the tests:
`python3 manage.py test stations/tests`

Database Diagram:

Application pages: