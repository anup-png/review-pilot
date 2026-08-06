from typing import TypedDict,Literal

class ReviewState(TypedDict):

    review:str
    sentiment:Literal["negative","positive","neutral"]
    description:str
    reply:str
