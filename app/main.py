from fastapi import FastAPI, status

from app.config.database import get_db

app = FastAPI()


@app.get(
    "/health",
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
def health_check():
    return {"message": "Server is up and running..."}


try:
    get_db().command("ping")
    print("Connected to Database successfully...")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
