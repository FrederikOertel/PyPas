"""Group model."""
from dataclasses import dataclass
from enum import Enum
from typing import List


class GroupType(Enum):
    """Describes the type of group."""

    Vault = 1
    Directory = 2


@dataclass
class GroupMember:
    """Describes a member of a group."""

    id: int
    UserName: str


@dataclass
class Group:
    """Describe a group with its properties and members."""

    id: int
    groupType: GroupType
    groupName: str
    description: str
    location: str
    directory: str
    dn: str
    members: List[GroupMember]
