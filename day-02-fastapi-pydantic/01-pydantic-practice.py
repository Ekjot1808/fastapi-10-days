from pydantic import BaseModel, Field

class Product(BaseModel): # Base model provides data validation and serrialization
    name: str = Field(min_length=3)
    price: float = Field(gt=0) 
    quantity: int = Field(ge=1, le=100) 
    category: str
    description: str | None = None # Optional field

product = Product(
    name="Iphone 13",
    price=80000.5,
    quantity=1,
    category="Phone"
)

print(product)