from langchain_core import output_parsers
from pydantic import BaseModel,Field
from typing import Literal

class ReviewAnalzer(BaseModel):

      sentiment:Literal["negative","positive",'neutral']=Field(description="tone of th user")
      description:str