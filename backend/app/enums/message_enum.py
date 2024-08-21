from enum import Enum as PyEnum


class MessageRoleEnum(PyEnum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"