# gas-station-data-manager

This app was created to help Gas Station owners manage their revenues, and related data, such as fuel types and price and discounts.

Front-End was taken from free Django-Pixel UI framework.

# Check it yourself!
[Gas station project deployed to Render](https://gas-station-data-manager.onrender.com/)

To test functionality use login data:
- `username: TestUser`
- `password: 2wsxvfr4`

# Lauching project locally

To launch the application, follow next steps:

1. Fork the repository

2. Clone it:
`git clone <here goes the HTTPS link you could copy on github repositiry page>`

3. Create a new branch:
`git checkout -b <new branch name>`

4. Create virtual environment:
`python3 -m venv venv`

5. Acivate venv:
`source venv/Scripts/activate`

6. Install requirements:
`pip3 install -r requirements.txt`

7. Run migrations:
`python3 manage.py migrate`

8. Load the data from fixture:
`python3 manage.py loaddata fixtures/db_data.json`

9. Run server:
`python3 manage.py runserver`

To run the tests:
`python3 manage.py test stations/tests`
# DB info
Database Diagram:
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/14c58b61-77d4-48a8-b604-2de70d2e2f8b)

# Demo
Application pages:
- Main Page
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/c2b8e07c-aed3-41c7-b11d-4e4aeedab5f3)
- Station List
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/7b0ddac4-d4a7-4171-b7b1-4b83749a1ad3)
- Station Detail
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/3bf43592-88cb-4207-9eaf-dfb494df3886)
- Station Create
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/5850f245-0f1c-416c-ae9c-47c760ddcf85)
- Station Delete
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/c55888b0-497a-45be-8589-3106f2ef238a)
- Station Update
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/7c6b69ae-5e69-48ab-a02f-3ca84b4ab079)
- Fuel List
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/fdd81113-b9f3-4753-b04e-65f016f7bcfb)
- Fuel Create
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/ecc8e8e6-be38-44a2-a1cf-b69bd396a0a5)
- Fuel Update
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/91d38de5-102c-4eca-aca3-570c3d5ecf0a)
- Fuel Delete
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/8d84a866-1332-4d80-8242-8ca1644af4bb)
- Manager List
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/46490a03-6bfd-4fc7-8c3c-d66a7d0004ef)
- Manager Profile
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/5a78b2a9-b5e3-4161-bfee-9c632c653495)
- Manager Create
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/a8b80548-230c-47b4-9f40-db034a3ed6c6)
- Manager Update
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/4d450a0f-cfed-4d29-9976-ff35a1b3612e)
- Manager Delete
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/b4a1a20d-ccc4-4de2-ab0c-8500758cd823)
- Discount List
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/62fb3dce-637d-45f3-9755-a8708fdb93aa)
- Discount Create
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/7b2ab562-a71d-497e-a9c3-b0e7ede262b6)
- Discount Update
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/f2410816-b086-44e8-9278-b2cfc394626f)
- Diacount Delete
![image](https://github.com/Lyutillis/gas-station-data-manager/assets/62535257/c0314b6f-de3a-4690-abcb-d63a8100ad22)
