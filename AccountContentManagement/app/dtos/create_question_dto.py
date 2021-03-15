from dataclasses import dataclass


@dataclass
class CreateQuestionDto:
    content: str
    type: int
