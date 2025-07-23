from pydantic import BaseModel, UUID4, constr, condecimal
from typing import Annotated
from datetime import datetime

# Correct type aliases using Annotated
AccountType = Annotated[str, constr(to_lower=True)]
DepositAmount = Annotated[float, condecimal(decimal_places=2, ge=0)]
BalanceAmount = Annotated[float, condecimal(decimal_places=2)]

class AccountCreate(BaseModel):
    customer_id: UUID4
    account_type: AccountType
    initial_deposit: DepositAmount

class AccountResponse(AccountCreate):
    id: UUID4
    account_number: str
    balance: BalanceAmount
    created_at: datetime

    class Config:
        orm_mode = True
