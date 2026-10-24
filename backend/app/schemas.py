from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str

class ItemOut(ItemCreate):
    id: int

    class Config:
        from_attributes = True