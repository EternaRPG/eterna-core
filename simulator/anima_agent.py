from agentpy import Agent
from anima_entity import AnimaEntity

class AnimaAgent(Agent):
    def setup(self):
        self.type = self.p.type or 'NPC'
        self.pos = self.p.pos or None
        self.fsm = self.p.fsm or None
        self.flags = {}
        self.state = None

    def move_to(self, x: int, y: int):
        self.pos = (x, y)

    def set_flag(self, key: str, value: bool = True):
        self.flags[key] = value

    def clear_flag(self, key: str):
        if key in self.flags:
            del self.flags[key]

    def has_flag(self, key: str) -> bool:
        return self.flags.get(key, False)

    def __repr__(self):
        return f'<Agent {self.id} ({self.type}) at {self.pos}>'
