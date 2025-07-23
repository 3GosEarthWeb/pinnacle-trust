from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth_router, user_router, account_router, transaction_router, loan_router, admin_router

app = FastAPI(title="Pinnacle Trust API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}

app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(account_router.router, prefix="/accounts", tags=["Accounts"])
app.include_router(transaction_router.router, prefix="/transactions", tags=["Transactions"])
app.include_router(loan_router.router, prefix="/loans", tags=["Loans"])
app.include_router(admin_router.router, prefix="/admin", tags=["Admin"])
