from dataclasses import dataclass


@dataclass
class CreateQuestionDto:
    content: str
    tag: str = ""
    type: int = 1
