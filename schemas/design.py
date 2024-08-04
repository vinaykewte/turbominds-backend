from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, UUID4


class GenerateDesign(BaseModel):
    context: str
