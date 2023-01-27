from typing import Optional
from pydantic import BaseModel
  
class Pot(BaseModel):
    id: Optional[str]
    total: int