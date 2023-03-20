from pydantic import BaseModel


class GroupBase(BaseModel):
    name: str


class GroupModel(GroupBase):
    pass
    
    
class GroupUpdate(GroupBase):
    pass


class GroupRepsponse(GroupBase):
    id: int
    
    class Config:
        orm_mode = True