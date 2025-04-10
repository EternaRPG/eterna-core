import random

class AnimaEntity:
    def __init__(
        self,
        name: str = f"Entity {random.randint(100,999)}",
        description: str = '',
        animus: int = random.randint(30, 300),
    ):
        self.name = name
        self.animus = animus
