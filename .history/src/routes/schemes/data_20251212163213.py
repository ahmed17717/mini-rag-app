from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
  file_id: str
  chunk_size: 