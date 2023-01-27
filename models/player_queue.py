from typing import Optional
from pydantic import BaseModel
  
class Queue(BaseModel):
    id: Optional[str]
    queue: list