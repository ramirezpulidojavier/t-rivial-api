from typing import Optional
from pydantic import BaseModel
  
class Couple(BaseModel):
    player1: str
    player2: str