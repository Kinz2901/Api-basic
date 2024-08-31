from pydantic import BaseModel, Field


class RequestLogin(BaseModel):
    username: str = Field(...,min_length=3, max_length=50)
    password: str = Field(...,min_length=3, max_length=50)



#test fail
test = RequestLogin(username="tt", password="tt")
