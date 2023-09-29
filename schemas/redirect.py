from pydantic import BaseModel, Field
from typing import List


class UserServiceCreateBodySchema(BaseModel):
    """
        Defines the parameters for creating a user inside database
    """

    username: str = Field(description="user's username", example="TestUser")
    password: str = Field(description="user's password",
                          example="mytestpasswrod")


class HeaderSchema(BaseModel):
    """
        Header Schema used for receiving token inside Authorization Header
    """
    authorization: str = Field(...,
                               alias="Authorization", example='Authorization Bearer JWT_TOKEN')


class ProductServiceSearchSchema(BaseModel):
    """ Product will be searched by name
    """
    name: str = Field(example="Detergente",
                      description="Name of the product that you want to search for")


class ProductServiceCreateOrderSchema(BaseModel):
    """
        Parameters for successfully create an order
    """
    user_email: str = 'test@email.com'
    total_price: float = 120.00
    date: str = '2023-09-20T19:15:24.588Z'
    order_products: List = [
        {"amount": 3, "price": 10.99, "product_id": 1},
        {"amount": 6, "price": 1.99, "product_id": 2},
        {"amount": 7, "price": 15.99, "product_id": 3},
    ]


class ProductServiceProductPathSchema(BaseModel):
    """ Defines the url path product id
    """
    product_id: int = Field(description="Product id")


class ProductServiceCreateProductSchema(BaseModel):
    """ Arguments needed for creating a product in the database
    """

    name: str = Field(example='Detergente para mãos')
    description: str = Field(
        example='Detergente potente para retirar todos os resíduos')
    amount: int = Field(example=3)
    weight: str = Field(example='1L')
    image: str = Field(example='https://example.com')
    price: float = Field(example=50.99)
