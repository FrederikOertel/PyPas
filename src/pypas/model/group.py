from dataclasses import dataclass
from enum import Enum
from typing import List

class GroupType(Enum):
    Vault = 1
    Directory = 2

@dataclass
class GroupMember:
    id: int
    UserName: str

@dataclass
class Group:
    id: int
    groupType: GroupType
    groupName: str
    description: str
    location: str
    directory: str
    dn: str
    members: List[GroupMember]
