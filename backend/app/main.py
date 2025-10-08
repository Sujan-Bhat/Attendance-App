from fastapi import FastAPI

app = FastAPI(title="Attendance Management System API")

@app.get("/", tags=["Root"])

async def read_root():

    """Call this root endpoint to check if the service is up and running."""
    return {"status": "ok", "message": "Welcome to the Attendance Management System API"}

# Additional endpoints and logic would go here