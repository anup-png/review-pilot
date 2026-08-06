from typing import TypedDict,Literal

class reviewState(TypedDict):

    review:str
    sentiment:Literal["negative","positive","neutral"]
    reply:str
