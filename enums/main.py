from enum import Enum

class FunctionStates(Enum):
    ACTIVE = 1
    PASSIVE = 2

# Usage
print(FunctionStates.ACTIVE)  # FunctionStates.ACTIVE
print(FunctionStates.ACTIVE.value)  # 1

state = FunctionStates.ACTIVE
print(state.name)   # 'ACTIVE'
print(state.value)  # 1