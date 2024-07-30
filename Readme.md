  

# Daily Expenses Sharing Application

  

This project is a Daily Expenses Sharing Application built with FastAPI, SQLAlchemy, and SQLite. It allows users to share and manage daily expenses with ease, providing multiple ways to split expenses and generating balance sheets for download.

  

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


## Getting Started

  

### Prerequisites

  

- Python 3.8+

- SQLite (included with Python)

  

### Installation

  

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

1. Initialize the database:

```bash
python -m app.main
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

- **Note**: for each instance of {id}, copy the id returned while creating a user

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