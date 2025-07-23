from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.status import HTTP_200_OK

# Import your routers
from app.api.auth_router import router as auth_router
from app.api.user_router import router as user_router
# Add more router imports here as you generate them

app = FastAPI(
    title="Pinnacle Trust API",
    version="1.0.0",
    description="Backend API for Pinnacle Trust Banking System",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS (adjust origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/health", status_code=HTTP_200_OK)
def health_check():
    return {"status": "ok"}

# Register routers
app.include_router(auth_router)
app.include_router(user_router)
# Add more include_router(...) as needed

