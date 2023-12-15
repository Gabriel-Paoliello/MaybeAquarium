
from enum import Enum
from typing import TypeVar

from models.Entity import Entity
from typing import Type, Any

EntityType = TypeVar('EntityType', bound=Entity)

class MoveDecision(Enum):
    RUN_FROM = 1
    RUN_TO = 2

class MoveEntityDecision():
    def __init__(self, entityType: Type[EntityType], decision: MoveDecision):
        self.entity = entityType
        self.decision = decision
    