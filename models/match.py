from typing import Optional
from pydantic import BaseModel
from datetime import datetime
  
class Match(BaseModel):
    id: Optional[str]
    player1: str
    player2: Optional[str]
    result: str
    date: datetime
    pot: Optional[int]