from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
#from app.api.v1 import auth, teacher, attendance, analytics

app = FastAPI(title=settings.PROJECT_NAME)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# # Include routers
# app.include_router(auth.router, prefix=settings.API_V1_STR)
# app.include_router(teacher.router, prefix=settings.API_V1_STR)
# app.include_router(attendance.router, prefix=settings.API_V1_STR)
# app.include_router(analytics.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to Attendance Management System"}