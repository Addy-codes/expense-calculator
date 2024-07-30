from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api import user, expense
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Daily Expenses Sharing Application",
    description="A backend for managing daily expenses and splitting them among users.",
    version="1.0.0"
)

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(user.router, prefix="/api/v1/user", tags=["users"])
app.include_router(expense.router, prefix="/api/v1/expenses", tags=["expenses"])

@app.get("/")
def read_root():
    """
    Root endpoint welcoming users to the Daily Expenses Sharing Application API.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Welcome to the Daily Expenses Sharing Application API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
