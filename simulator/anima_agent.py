from agentpy import Agent
from anima_entity import AnimaEntity

class AnimaAgent(Agent):
    def setup(self):
        self.entity = self.p.entity
