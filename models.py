from datetime import datetime, timezone
from typing import Annotated, Optional

from pydantic import BaseModel, ConfigDict, Field


class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: Annotated[str | None, Field(max_length=100)]
    description: Annotated[Optional[str] | None, Field(max_length=255)]
    priority: Annotated[str | None, Field()] = "low"
    is_done: Annotated[bool | None, Field()] = False
    is_deleted: Annotated[bool | None, Field()] = False
    created_at: Annotated[datetime | None, Field()] = datetime.now(timezone.utc)
