from pydantic import BaseModel
from datetime import datetime
class TransactionInDB(BaseModel):
    username: str
    value: int


class TransactionOut(BaseModel):
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_balance: int

database_transactions = []
generator = {"id":0}
def save_transaction(transaction_in_db: TransactionInDB):
    generator["id"] = generator["id"] + 1
    transaction_in_db.id_transaction = generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db