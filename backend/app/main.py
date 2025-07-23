from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.api.v1 import (
    auth, users, accounts, transactions, loans,
    dashboard, support, analytics, audit, notifications
)

from app.core.config import settings
from app.core.logger import setup_logging

# Initialize logging
setup_logging()

app = FastAPI(
    title="Pinnacle Trust Banking API",
    description="Secure API for banking operations and admin control",
    version="1.0.0"
)

# Enable CORS
origins = [
    "http://localhost:3000",  # React dev
    "https://your-frontend-domain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static directory (optional)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include API routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(accounts.router, prefix="/api/v1")
app.include_router(transactions.router, prefix="/api/v1")
app.include_router(loans.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")
app.include_router(support.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1")
app.include_router(audit.router, prefix="/api/v1")
app.include_router(notifications.router, prefix="/api/v1")

# Custom error handler (example)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred."}
    )

# Health check route
@app.get("/health")
def health_check():
    return {"status": "ok"}

