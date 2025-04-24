# src/config.py
from pydantic import BaseModel, validator

class VMConfig(BaseModel):
    name: str
    os: str
    cpu: int
    ram: int

    @validator('cpu')
    def validate_cpu(cls, v):
        if v < 1:
            raise ValueError("CPU must be greater than zero")
        return v

    @validator('ram')
    def validate_ram(cls, v):
        if v < 1:
            raise ValueError("RAM must be greater than zero")
        return v

