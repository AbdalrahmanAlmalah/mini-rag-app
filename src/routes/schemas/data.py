from pydantic import BaseModel, Field
from typing import Optional

class ProcessRequest(BaseModel):
    """
    Request model for processing data.
    """
    file_id: str  
    chunk_size: Optional[int] = 100
    overlap_size:Optional[int] = 20
    do_rest: Optional[int] = 0
    