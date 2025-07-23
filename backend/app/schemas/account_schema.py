from pydantic import BaseModel, UUID4, constr, condecimal
from datetime import datetime

class AccountCreate(BaseModel):
    customer_id: UUID4
    account_type: constr(to_lower=True)
    initial_deposit: condecimal(decimal_places=2, ge=0)

class AccountResponse(AccountCreate):
    id: UUID4
    account_number: str
    balance: condecimal(decimal_places=2)
    created_at: datetime

    class Config:
        orm_mode = True
