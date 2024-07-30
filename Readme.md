  

# Daily Expenses Sharing Application

This project is a Daily Expenses Sharing Application built with FastAPI, SQLAlchemy, SQLite and Docker. It allows users to share and manage daily expenses with ease, providing multiple ways to split expenses and generating balance sheets for download.

This Backend Web-Service is deployed on Render: https://expense-calculator-tlbo.onrender.com/docs


## Features

  

-  **User Management**: Add and retrieve users.

-  **Expense Management**:

- Add expenses.

- Retrieve individual user expenses.

- Retrieve overall expenses.

- Download balance sheets showing individual and overall expenses.

-  **Expense Splitting Methods**:

- Equal: Split equally among all participants.

- Exact: Specify the exact amount each participant owes.

- Percentage: Specify the percentage each participant owes (ensuring percentages add up to 100%).


## Screenshots
- Create User
![image](https://github.com/user-attachments/assets/50f0746e-c7fb-4d3b-b104-8c95de149596)
- Create Expense
![image](https://github.com/user-attachments/assets/eb53332c-1f0b-43f4-879d-32dcbd4dd23b)
- Downloaded Balance Sheet
![image](https://github.com/user-attachments/assets/c8bbc608-c158-4deb-ac03-ce5d8dcd6015)


### Prerequisites

  

- Python 3.8+

- SQLite (included with Python)

- Docker

### Installation

  

1. Clone the repository:

  

```bash
git clone https://github.com/Addy-codes/expense-calculator.git
cd expense-calculator
```


2. Create a .env file and paste the below text:

```
SQLALCHEMY_DATABASE_URL=sqlite:///./test.db
```

3. Run the service using docker

```bash
docker build -t daily-expenses-app .
docker run -d -p 8000:8000 --name daily-expenses-container daily-expenses-app
```

This command will start a Docker container from the daily-expenses-app image and map port 8000 on your host to port 8000 in the container.

### Manual Installation

  

1. Clone the repository:

  

```bash
git clone https://github.com/Addy-codes/expense-calculator.git
cd expense-calculator
```


2. Create a virtual environment and activate it:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

### Database Setup

1. Create a .env file and paste the below text:

```bash
SQLALCHEMY_DATABASE_URL=sqlite:///./test.db
```

### Running the Application

  

1. Start the FastAPI server:

  

```bash
uvicorn app.main:app --reload
```

  

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI for API documentation and testing.

  

## API Endpoints

  

### User Endpoints

  

-  **Add user**: `POST /api/v1/user/`

-  **Retrieve user**: `GET /api/v1/user/{user_id}`

  

### Expense Endpoints

  

-  **Add expense**: `POST /api/v1/expenses/`

-  **Retrieve individual user expenses**: `GET /api/v1/expenses/user/{user_id}`

-  **Retrieve overall expenses**: `GET /api/v1/expenses/`

-  **Download balance sheet**: `GET /api/v1/expenses/balance-sheet`

  

## Sample Data
  

### Create User

  

```json
{
"email": "adeeb@convin.in",
"name": "Adeeb",
"mobile_number": "1234567890"
}
```

  

### Create Expense

- **Note**: for each instance of {id}, copy the id returned while creating a user. If you're using the deployed version on render, you can use the below two id's

```
78c3a591-6591-49f0-96e4-fde1322fd074
d3ce59cf-cdd9-4804-b30a-00c22cb94f54
```

#### Equal Split

  

```json
{
"description": "Team lunch",
"amount": 120.0,
"split_type": "equal",
"participants": [
{
"user_id": "{id}",
"amount": null,
"percentage": null
},
{
"user_id": "{id}",
"amount": null,
"percentage": null
}
],
"created_by": "{id}"
}
```

  

### Exact Split

  

```json
{
"description": "Office supplies",
"amount": 150.0,
"split_type": "exact",
"participants": [
{
"user_id": "{id}",
"amount": 80.0,
"percentage": null
},
{
"user_id": "{id}",
"amount": 70.0,
"percentage": null
}
],
"created_by": "{id}"
}
```

  

### Percentage Split

```json
{
"description": "Project celebration dinner",
"amount": 200.0,
"split_type": "percentage",
"participants": [
{
"user_id": "{id}",
"amount": null,
"percentage": 60.0
},
{
"user_id": "{id}",
"amount": null,
"percentage": 40.0
}
],
"created_by": "{id}"
}
```
