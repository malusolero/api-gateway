from pydantic import BaseModel, Field
from typing import Optional


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
    authorization: Optional[str] = Field(
        alias="Authorization", example='Authorization Bearer JWT_TOKEN')
